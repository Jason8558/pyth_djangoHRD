from django.shortcuts import render, redirect
from .models import *
from .forms import *
from TURV.models import TabelItem
from TURV.models import Department
from TURV.models import Employers
from .additionals import *
from django.http import HttpResponse, JsonResponse

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
            form.fields['emps'].queryset = Employers.objects.filter(department=form['dep'].value())
            if form.is_valid():

                form.saveAll()
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

        shed_info = ShiftShedModel.objects.get(id=id)

        return render(request, 'shift_shed/shedule.html', context={'shedule':shedule, 'shed_info':shed_info, 'months':months, 'days':days, 'id':id})

def ss_edit(request,shed,month,year):
    if request.user.is_authenticated:

        
        items = addition_formforedit(shed, month)
        months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
        return render(request, 'shift_shed/shedule_single.html', context={'items':items, 'year':year, 'month':months
        [str(month)], 'month_dig':month, 'shed':shed})

def ss_item_add(request, shed, month):
    if request.user.is_authenticated:
        current_shed = ShiftShedModel.objects.get(id=shed)
        items = Employers.objects.filter(department=current_shed.dep).filter(fired=0).filter(mainworkplace=1)
        months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
        if request.method == 'GET':
            form = SS_AddItem_form(request.GET)
            form.fields['employer'].queryset = Employers.objects.filter(department=current_shed.dep).filter(fired=0).filter(mainworkplace=1)


        return render(request, 'shift_shed/new_shed_item.html', context={'emps':items, 'shed':current_shed, 'month':months
        [str(month)], 'form':form})
