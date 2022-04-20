from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from TURV.models import Employers
from itertools import groupby

def ugroup(request):
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


def vacsheds(request):
    if request.user.is_authenticated:
        if ugroup(request) == True:
            vacsheds = VacantionShedule.objects.all()
        return render(request, 'VacShed/index.html', context={'vacsheds':vacsheds})
    else:
        return redirect('/accounts/login/')

def vacshed_create(request,vs):
    if request.user.is_authenticated:
        vacshed = VacantionShedule.objects.get(id=vs)

        return render(request, 'VacShed/vs-create.html', context={'vacshed':vacshed})

def getvacshed_json(request, vs):
    if request.user.is_authenticated:
        items = VacantionSheduleItem.objects.filter(bound_shed=vs).values('id', 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__cat__name').order_by('emp', 'id', 'dur_from')
        items = list(items)
        return JsonResponse(items, safe=False)

def vacshed_addItem(request,id):
    if request.user.is_authenticated:
        vacshed = VacantionShedule.objects.get(id=id)
        employers = Employers.objects.filter(department_id=vacshed.dep_id)
        employers = list(employers)
        if request.method == 'GET':
            return render(request, 'VacShed/new_item.html', context={'vacshed':vacshed})
        if request.method == 'POST':
            periods = request.POST.get('vac-form-all-periods')
            for per in periods.split('|'):
                if per != '':
                    print(per)
            return render(request, 'VacShed/new_item.html', context={'vacshed':vacshed})


def getemployers(request, dep):
    if request.user.is_authenticated:
        emps = Employers.objects.filter(department_id=dep).values('id','fullname','position__name').order_by('fullname')
        emps = list(emps)
        return JsonResponse(emps, safe=False)
