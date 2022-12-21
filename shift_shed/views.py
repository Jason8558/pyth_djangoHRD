from django.shortcuts import render, redirect
from .models import *
from .forms import *
from TURV.models import TabelItem
from TURV.models import Department
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
                print('here')
                form.saveAll()
                return redirect('/shift_shed/')
            else:
                return render(request, 'shift_shed/create.html', context={'form':form})


def ss_get_employers(request, dep):
    if request.user.is_authenticated:
        emps = Employers.objects.values('id','fullname','position__name').filter(mainworkplace=1).filter(fired=0).filter(department=dep)
        emps = list(emps)
        return JsonResponse(emps, safe=False)

def ss_shedule(request, id):
    if request.user.is_authenticated:
        # emps = [2709,37,207,227]
        days = []
        for i in range(1,32):
            days.append(i)
        months = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
        shedule = addition_shedform(id)
        return render(request, 'shift_shed/shedule.html', context={'shedule':shedule, 'months':months, 'days':days})
