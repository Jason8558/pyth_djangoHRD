from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from TURV.models import TabelItem
from TURV.models import Department
from TURV.models import Employers
from TURV.models import Overtime
from vac_shed.models import VacantionSheduleItem
from .additionals import *
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

def ss_main(request):
    if request.user.is_authenticated:
        ss = ShiftShedModel.objects.all()

        return render(request, 'shift_shed/ss-main.html', context={'ss':ss})

def ss_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = ShiftShed_form(request.GET)
            form.fields['dep'].queryset = Department.objects.filter(user=request.user)
            return render(request, 'shift_shed/create.html', context={'form':form})
        if request.method == 'POST':
            form = ShiftShed_form(request.POST)
            form.fields['dep'].queryset = Department.objects.filter(user=request.user)
            # form.fields['emps'].queryset = Employers.objects.filter(department=form['dep'].value())
            if form.is_valid():

                form.save()
                return redirect('/shift_shed/')
            else:
                return render(request, 'shift_shed/create.html', context={'form':form})


def ss_get_employers(request, dep):
    if request.user.is_authenticated:
        emps = Employers.objects.values('id','fullname','position__name').filter(mainworkplace=1).filter(fired=0).filter(department=dep)
        emps = list(emps)
        return JsonResponse(emps, safe=False)
    
def ss_get_emp_single(request, id):
    if request.user.is_authenticated:
        emp = Employers.objects.filter(id=id).values('id', 'fullname', 'sex', 'level', 'position__name', 'positionOfPayment', 'shift_personnel', 'stand_worktime')
        emp = list(emp)
        return JsonResponse(emp, safe=False)

def ss_shedule(request, id):
    if request.user.is_authenticated:
        # emps = [2709,37,207,227]
        
        days = []
        for i in range(1,32):
            days.append(i)
        months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
        shedule = addition_shedform(id)
        total = additional_formtotal(id)

        shed_info = ShiftShedModel.objects.get(id=id)

        return render(request, 'shift_shed/shedule.html', context={'shedule':shedule, 'shed_info':shed_info, 'months':months, 'days':days, 'id':id, 'total':total})

def ss_edit(request,shed,month,year):
    if request.user.is_authenticated:

        shed_info = ShiftShedModel.objects.get(id=shed)
        items = addition_formforedit(shed, month)
        months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
        return render(request, 'shift_shed/shedule_single.html', context={'items':items, 'year':year, 'month':months
        [str(month)], 'month_dig':month, 'shed':shed, 'shed_info':shed_info})

def ss_item_add(request, shed, month):
    if request.user.is_authenticated:
        current_shed = ShiftShedModel.objects.get(id=shed)
        items = Employers.objects.filter(department=current_shed.dep).filter(fired=0).filter(mainworkplace=1)
        months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
        if request.method == 'GET':
            form = SS_AddItem_form(request.GET)
            form.fields['employer'].queryset = Employers.objects.filter(department=current_shed.dep).filter(fired=0).filter(mainworkplace=1)
        else:
            form = SS_AddItem_form(request.POST)
            if form.is_valid():
                form.saveFirst(shed,month)
                return redirect
            else:
                print(form.errors.as_text)

        return render(request, 'shift_shed/new_shed_item.html', context={'emps':items, 'shed':current_shed, 'month':months
        [str(month)], 'month_dig':month, 'form':form})

@login_required   
def ss_get_vacantions(request,emp, month, year):
    v_items = VacantionSheduleItem.objects.filter(emp_id=emp).filter(bound_shed__year=year).filter(Q(dur_from__month=month) | Q(dur_to__month=month))
    emp_ = Employers.objects.get(id=emp)
    if emp_.sex == 'М':
        norm = Overtime.objects.get(year__year=year).value_m
    else:
        norm = Overtime.objects.get(year__year=year).value_w 

    print(norm)

    days = list()
    vac_info = list()
    for item in v_items:
        if int(str(item.dur_to).split('-')[1]) == int(str(item.dur_from).split('-')[1]):
            # m_range = calendar.monthrange(int(year),int(month))
            for i in range(int(str(item.dur_from).split('-')[2]), int(str(item.dur_to).split('-')[2])+1):
                days.append(i)
        else:
            if int(str(item.dur_from).split('-')[1]) == int(month):
                m_end = calendar.monthrange(int(year), int(month))
                for i in range (int(str(item.dur_from).split('-')[2]), m_end[1]+1):
                    days.append(i)
            
            if int(str(item.dur_to).split('-')[1]) == int(month):
                for i in range (1, int(str(item.dur_to).split('-')[2])+1):
                    days.append(i)
    vac_info.append({
        'emp':emp,
        'days':days,
        'norm':norm
    })

    return JsonResponse(vac_info, safe=False)



