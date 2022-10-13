from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from TURV.models import Employers
from TURV.models import Department
from itertools import groupby
from .forms import *


def current_user(request):
    return request.user.id

def ugroup(request):
        # Проверка на права пользователя
        user_ = request.user
        u_group = user_.groups.all()

        granted = 0
        for group in u_group:
            if (group.name == 'Сотрудник СУП') or (group.name == 'Сотрудник РО'):
                granted = 1
        if user_.is_superuser:
            granted = 1

        return granted

def vacshed_new(request):
    if request.user.is_authenticated:
        user_ = request.user
        u_group = user_.groups.all()
        granted = 0

        for group in u_group:
            if group.name == 'Сотрудник СУП':
                granted = 1
        if (request.user.is_superuser) or (granted == 1):
            vacshed_form = Vacshed_form(user_id='all')
        else:
            vacshed_form = Vacshed_form(user_id=current_user(request))


        if request.method == "POST":
            vacshed_form = Vacshed_form(request.POST)
            if vacshed_form.is_valid():
                user_ = request.user.first_name
                vacshed_form.saveFirst(user_)
                return redirect('/vacshed/')
            else:
                return render(request, 'vac_shed/new_vacshed.html', context={ 'form':vacshed_form})

        else:

            return render(request, 'vac_shed/new_vacshed.html', context={ 'form':vacshed_form})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def vacshed_global_json(request, year):
    if request.user.is_authenticated:
        items = VacantionSheduleItem.objects.filter(bound_shed__year=year).values('id', 'bound_shed__dep__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('bound_shed__dep__name', 'emp', 'id', 'dur_from')
        items = list(items)
        return JsonResponse(items, safe=False)

def vacshed_global_create(request):
    if request.user.is_authenticated:
        return render(request, 'vac_shed/vs-global.html')

def vacsheds(request):
    if request.user.is_authenticated:
        print(ugroup(request))
        if ugroup(request) == 1:
            vacsheds = VacantionShedule.objects.all()
        else:
            deps = Department.objects.filter(user=current_user(request)).values('id')
            vacsheds = VacantionShedule.objects.filter(dep__in=deps)
        return render(request, 'vac_shed/index.html', context={'vacsheds':vacsheds, 'granted':ugroup(request)})
    else:
        return redirect('/accounts/login/')

def vacshed_create(request,vs):
    if request.user.is_authenticated:
        granted = ugroup(request)
        vacshed = VacantionShedule.objects.get(id=vs)

        return render(request, 'vac_shed/vs-create.html', context={'vacshed':vacshed, 'granted':granted})

def getvacshed_json(request, vs):
    if request.user.is_authenticated:
        items = VacantionSheduleItem.objects.filter(bound_shed=vs).values('id', 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp', 'id', 'dur_from')
        items = list(items)
        return JsonResponse(items, safe=False)

def vacshed_addItem(request,id):
    if request.user.is_authenticated:
        vacshed = VacantionShedule.objects.get(id=id)
        employers = Employers.objects.filter(department_id=vacshed.dep_id).filter(fired=0)
        employers = list(employers)
        if request.method == 'GET':
            return render(request, 'vac_shed/new_item.html', context={'vacshed':vacshed})
        if request.method == 'POST':
            periods = request.POST.get('vac-form-all-periods')
            empl = request.POST.get('vac_emp')
            dfrom = request.POST.get('per-date-from')
            dto = request.POST.get('per-date-to')
            dcount = request.POST.get('per-days-count')
            city = request.POST.get('city')
            child = request.POST.get('child')

            periods = periods.split('|')

            for i in range(len(periods)):
                if periods[i] != '':
                    print(i)
                    if i == 0:
                        VacantionSheduleItem.objects.create(
                            emp = Employers.objects.get(id=empl),
                            dur_from = periods[i].split(':')[0],
                            dur_to = periods[i].split(':')[1],
                            days_count = periods[i].split(':')[2],
                            bound_shed = vacshed,
                            city = city,
                            child_year = child
                        )
                    else:
                        VacantionSheduleItem.objects.create(
                            emp = Employers.objects.get(id=empl),
                            dur_from = periods[i].split(':')[0],
                            dur_to = periods[i].split(':')[1],
                            days_count = periods[i].split(':')[2],
                            bound_shed = vacshed,

                        )

            return render(request, 'vac_shed/new_item.html', context={'vacshed':vacshed})

def vacshed_updItem(request, id, type):
    if request.user.is_authenticated:
        ndatefrom = request.POST.get('per-date-from')
        ndateto = request.POST.get('per-date-to')
        ndayscount = request.POST.get('per-days-count')
        ncity = request.POST.get('city')
        nchild = request.POST.get('child')
        item = VacantionSheduleItem.objects.get(id=id)
        if request.method == 'GET':
            return render(request, 'vac_shed/upd_item.html', context={'item':item, 'type':type})
        else:

            if type != 1:
                item.dur_from = ndatefrom
                item.dur_to = ndateto
                item.days_count = ndayscount
                item.save()
            else:
                 item.city = ncity
                 item.child_year = nchild
                 item.save()
            return redirect('/vacshed/create/' + str(item.bound_shed.id) + '/')




def getemployers(request, dep):
    if request.user.is_authenticated:
        emps = Employers.objects.filter(department_id=dep).filter(fired=0).values('id','fullname','position__name').order_by('fullname')
        emps = list(emps)
        return JsonResponse(emps, safe=False)
