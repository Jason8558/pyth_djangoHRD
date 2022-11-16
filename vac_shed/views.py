from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from TURV.models import Employers
from TURV.models import Department
from itertools import groupby
from .forms import *
from django.db.models import Sum, F, Case, When, Q


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

def vacshed_global_json(request, year, dep, per, emps, fil_only, terr):
    if request.user.is_authenticated:
        if dep !=0 and per != 0:
            items_main = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp__department_id = dep).filter(dur_from__month=per).exclude(move_from__isnull=False).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name', 'emp', 'id', 'dur_from')
            items_move = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp__department_id = dep).filter(move_from__month=per).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
            items = items_main.union(items_move).order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')

        else:
            if dep != 0:
                items = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp__department_id = dep).values('id', 'emp__department__name' , 'emp__aup__name' ,'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                items_aup = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp__aup_id = dep).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                items = items_aup.union(items).order_by('emp__department__name','emp__aup__name', 'emp__fullname', 'id', 'dur_from')
                if dep == 4:
                    items = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp__department_id__in = [4,31]).values('id', 'emp__department__name' , 'emp__aup__name' ,'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
            else:
                if per != 0:
                    if terr == 1:
                        items_main = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(dur_from__month=per).filter(~Q(emp__department__name__contains='Елизово')).exclude(move_from__isnull=False).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                        items_move = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(move_from__month=per).filter(~Q(emp__department__name__contains='Елизово')).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                        items = items_main.union(items_move).order_by('emp__department__name', 'emp__fullname', 'id', 'dur_from')
                    if terr == 2:
                        items_main = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(dur_from__month=per).filter(emp__department__name__contains='Елизово').exclude(move_from__isnull=False).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                        items_move = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(move_from__month=per).filter(emp__department__name__contains='Елизово').values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                        items = items_main.union(items_move).order_by('emp__department__name', 'emp__fullname', 'id', 'dur_from')
                    if terr == 0:
                        items_main = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(dur_from__month=per).exclude(move_from__isnull=False).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                        items_move = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(move_from__month=per).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                        items = items_main.union(items_move).order_by('emp__department__name', 'emp__fullname', 'id', 'dur_from')
                else:
                    if emps != '0':
                        emps_ = []
                        for e in emps.split(','):
                            if e != '':
                                print(e+'/n')
                                emps_.append(int(e))
                        items = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp_id__in=emps_).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')

                    else:
                        if terr == 1:
                            items = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(~Q(emp__department__name__contains='Елизово')).filter(bound_shed__dep__is_filial=0).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                        else:
                            if terr == 2:
                                items = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp__department__name__contains='Елизово').values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                            else:
                                if fil_only != 0:
                                    items = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(bound_shed__dep__is_filial=1).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')
                                else:
                                    items = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(bound_shed__dep__is_filial=0).values('id', 'emp__department__name' , 'emp__aup__name' , 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp__department__dir__name', 'emp__department__union__name', 'emp__aup__name', 'emp__department__name',  'emp', 'id', 'dur_from')


        items = list(items)
        return JsonResponse(items, safe=False)

def vacshed_global_create(request):
    if request.user.is_authenticated:
        deps = Department.objects.filter(notused=0)
        emps = Employers.objects.filter(fired=0).filter(mainworkplace=1)
        return render(request, 'vac_shed/vs-global.html', context={'deps':deps, 'emps':emps})

def vacsheds(request):
    if request.user.is_authenticated:
        print(ugroup(request))
        if ugroup(request) == 1:
            vacsheds = VacantionShedule.objects.all().exclude(dep__is_aup=1).order_by('year','dep__name')
        else:
            deps = Department.objects.filter(user=current_user(request)).values('id')
            vacsheds = VacantionShedule.objects.filter(dep__in=deps)
        return render(request, 'vac_shed/index.html', context={'vacsheds':vacsheds, 'granted':ugroup(request)})
    else:
        return redirect('/accounts/login/')

def vacsheds_aup(request):
    if request.user.is_authenticated:
        deps = Department.objects.filter(is_aup=1).values('id')
        vacsheds = VacantionShedule.objects.filter(dep__in=deps)
        return render(request, 'vac_shed/aup-vs.html', context={'vacsheds':vacsheds, 'granted':ugroup(request)})
    else:
        return redirect('/accounts/login/')

def vacshed_emp_info(request, year, emp):
    if request.user.is_authenticated:
        pers = VacantionSheduleItem.objects.filter(bound_shed__year=year).filter(emp_id=emp).values('id', 'bound_shed_id' ,'bound_shed__year', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'move_reason', 'child_year', 'days_count_move', 'city')
        city = ''
        child = ''
        vacshed = pers[0]['bound_shed_id']
        emp = pers[0]['emp__fullname']
        year = pers[0]['bound_shed__year']
        if len(pers) > 1:
            for per in pers:
                if per['city']:
                    city = per['city']
                if per['child_year']:
                    child = per['child_year']
    return render(request, 'vac_shed/emp-period.html', context={'pers':pers, 'city':city, 'child':child, 'emp':emp, 'year':year, 'vacshed':vacshed})




def vacshed_create(request,vs):
    if request.user.is_authenticated:
        granted = ugroup(request)
        vacshed = VacantionShedule.objects.get(id=vs)

        return render(request, 'vac_shed/vs-create.html', context={'vacshed':vacshed, 'granted':granted})

def getvacshed_json(request, vs):
    if request.user.is_authenticated:
        items = VacantionSheduleItem.objects.filter(bound_shed=vs).values('id', 'emp', 'emp__fullname', 'dur_from', 'dur_to', 'days_count', 'move_from', 'move_to', 'move_reason', 'child_year', 'days_count_move', 'city', 'emp__position__name').order_by('emp', 'dur_from')
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

        movefrom = request.POST.get('per-date-move-from')
        moveto = request.POST.get('per-date-move-to')
        daysmove = request.POST.get('per-days-move-count')
        movereason = request.POST.get('move-reason')


        item = VacantionSheduleItem.objects.get(id=id)
        if request.method == 'GET':
            return render(request, 'vac_shed/upd_item.html', context={'item':item, 'type':type})
        else:

            if type == 2:
                item.dur_from = ndatefrom
                item.dur_to = ndateto
                item.days_count = ndayscount
                item.save()
            else:
                if type == 1:
                    item.city = ncity
                    item.child_year = nchild
                    item.save()
                else:
                    if type == 3:
                        item.move_from = movefrom
                        item.move_to = moveto
                        item.move_reason = movereason
                        item.days_count_move = daysmove
                        item.save()
            return redirect('/vacshed/create/' + str(item.bound_shed.id) + '/')

def vacshed_check(request,id):
    if request.user.is_authenticated:
        vacshed = VacantionShedule.objects.get(id=id)

        if vacshed.sup_check == False:
            vacshed.sup_check = True
            vacshed.save()
        else:
            vacshed.sup_check = True
            vacshed.save()

    return redirect('/vacshed/create/' + str(id) + '/')




def getemployers(request, dep):
    if request.user.is_authenticated:
        emps = Employers.objects.filter(department_id=dep).filter(fired=0).filter(mainworkplace=1).values('id','fullname','position__name').order_by('fullname')
        emps_aup = Employers.objects.filter(aup_id=dep).filter(fired=0).filter(mainworkplace=1).values('id','fullname','position__name').order_by('fullname')
        emps = emps.union(emps_aup)
        emps = list(emps)
        return JsonResponse(emps, safe=False)

def delitem(request, id):
    if request.user.is_authenticated:
        item = VacantionSheduleItem.objects.get(id=id)
        item.delete()
    return redirect('/vacshed/create/' + str(item.bound_shed_id) + '/')
