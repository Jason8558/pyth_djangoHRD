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
from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, landscape
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.platypus import Paragraph


def access_check(request):
    # Проверка на права пользователя
    user_ = request.user
    u_group = user_.groups.all()

    granted = False
    for group in u_group:
        if (group.name == 'Сотрудник СУП') or (group.name == 'Сотрудник РО'):
            granted = True

    if request.user.is_superuser:
        granted = True
    return granted



def ss_main(request):
    if request.user.is_authenticated:
        if access_check(request) == True:
            ss = ShiftShedModel.objects.all()
        else:
            ss = ShiftShedModel.objects.filter(dep__user=request.user)
     
        return render(request, 'shift_shed/ss-main.html', context={'ss':ss})
    else:
        return redirect('/accounts/login/')

def ss_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = ShiftShed_form(request.GET)
            if access_check(request) == True:
                form.fields['dep'].queryset = Department.objects.filter(notused=0)
            else:
                form.fields['dep'].queryset = Department.objects.filter(user=request.user)
            return render(request, 'shift_shed/create.html', context={'form':form})
        if request.method == 'POST':
            form = ShiftShed_form(request.POST)
            if access_check(request) == True:
                form.fields['dep'].queryset = Department.objects.filter(notused=0)
            else:
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
        granted = False
        if request.user.is_superuser:
            granted = True    
        u_group = request.user.groups.all()

        for g in u_group:
            if g.name == 'Сотрудник СУП':
                granted = True

        days = []
        for i in range(1,32):
            days.append(i)
        months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
        shedule = addition_shedform(id)
        total = additional_formtotal(id)

        shed_info = ShiftShedModel.objects.get(id=id)

        return render(request, 'shift_shed/shedule.html', context={'shedule':shedule, 'granted':granted, 'shed_info':shed_info, 'months':months, 'days':days, 'id':id, 'total':total})

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
                
            else:
                print(form.errors.as_text)

        return render(request, 'shift_shed/new_shed_item.html', context={'emps':items, 'shed':current_shed, 'month':months
        [str(month)], 'month_dig':month, 'form':form})

@login_required
def ss_item_upd(request, id):
    item = ShiftShedItem.objects.get(id=id)
    emp = Employers.objects.get(id=item.employer.id)
    if emp.sex == 'М':
        norma = Overtime.objects.filter(year__year=item.bound_shed.year)[0].value_m
    else:
        norma = Overtime.objects.filter(year__year=item.bound_shed.year)[0].value_w
    print(norma)
    if request.method == 'GET':
        form = SS_AddItem_form(instance=item)
        return render(request, 'shift_shed/upd_shed_item.html', context={'item':item, 'form':form, 'main_norma':norma})
    if request.method == 'POST':
        form = SS_AddItem_form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect ('/shift_shed/shedule/' + str(item.bound_shed.id))
        # else:
        #     return render(request, 'shift_shed/upd_shed_item.html', context={'item':item, 'form':form, 'main_norma':norma})

@login_required
def ss_item_remove(request, id):
    item = ShiftShedItem.objects.get(id=id)
    item.delete()
    return redirect('/shift_shed/edit/' + str(item.bound_shed.id) + '/' + str(item.month) + '/' + str(item.bound_shed.year) )        

# # получаем отпуск выбранного работника
# @login_required   
# def ss_get_vacantions(request,emp, month, year):
#     v_items = VacantionSheduleItem.objects.filter(emp_id=emp).filter(bound_shed__year=year)
#     print(v_items)
#     emp_ = Employers.objects.get(id=emp)
#     if emp_.sex == 'М':
#         norm = Overtime.objects.get(year__year=year).value_m
#     else:
#         norm = Overtime.objects.get(year__year=year).value_w 

#     print(norm)

#     days = list()
#     vac_info = list()
#     for item in v_items:
#         m_from = int(str(item.dur_from).split('-')[1])
#         m_to = int(str(item.dur_to).split('-')[1])
#         y_from = int(str(item.dur_from).split('-')[0])
#         y_to = int(str(item.dur_to).split('-')[0])
        
#     if y_from == y_to: #если не переходит на след. год
#         if int(str(item.dur_to).split('-')[1]) == int(str(item.dur_from).split('-')[1]):
#             if m_from == month:
            
#                 for i in range(int(str(item.dur_from).split('-')[2]), int(str(item.dur_to).split('-')[2])+1):
#                     print(i)
#                     days.append(i)
#         else:
#             duration = m_to - m_from

#             for i in range(m_from, m_to):
                
#                 if i == month and month != m_from and month != m_to:
            
#                     for i in range (1, calendar.monthrange(int(year), int(month))[1]+1):
#                         days.append(i)
        
#                 if int(str(item.dur_from).split('-')[1]) == int(month):
              
#                     m_end = calendar.monthrange(int(year), int(month))
#                     for i in range (int(str(item.dur_from).split('-')[2]), m_end[1]+1):
#                         days.append(i)
                
#                 if int(str(item.dur_to).split('-')[1]) == int(month):
             
#                     for i in range (1, int(str(item.dur_to).split('-')[2])+1):
#                         days.append(i)
#     else:
#         if m_from == month:

#             for i in range(int(str(item.dur_from).split('-')[2]), ):
                
#                 days.append(i)    

                   
            
#     vac_info.append({
#         'emp':emp,
#         'days':days,
#         'norm':norm
#     })

#     return JsonResponse(vac_info, safe=False)


@login_required
def ss_set_checked(requset, id):
    shedule = ShiftShedModel.objects.get(id=id)
    
    if requset.method == 'GET':
        if shedule.checked == False:
            print(shedule.checked)
            shedule.checked = True
        else:
            shedule.checked = False
    
    shedule.save()
    
    return redirect('/shift_shed/shedule/' + str(shedule.id))

@login_required
def ss_change_comment(request, id):
    comment = request.GET.get('shedule-comment', '')
    shedule = ShiftShedModel.objects.get(id=id)
    shedule.comment = comment
    shedule.save()
    return redirect('/shift_shed/shedule/' + str(id))
