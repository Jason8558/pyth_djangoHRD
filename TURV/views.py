
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, F, Case, When, Q
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
import xlwt
from mimetypes import MimeTypes
import os
import datetime
from itertools import groupby
from reg_jounals.models import logs, logs_event
from django.contrib.auth.models import *
import json
from django.contrib.auth.decorators import login_required
from .additionals import *
from reg_jounals.views import get_rights

def w_close(request):
    return render(request, 'TURV/close.html')

def transliterate(name):
   """
   Автор: LarsKort
   Дата: 16/07/2011; 1:05 GMT-4;
   Не претендую на "хорошесть" словарика. В моем случае и такой пойдет,
   вы всегда сможете добавить свои символы и даже слова. Только
   это нужно делать в обоих списках, иначе будет ошибка.
   """
   # Слоаврь с заменами
   slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ja', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CZ','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}

   # Циклически заменяем все буквы в строке
   for key in slovar:
      name = name.replace(key, slovar[key])
   return name

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

# =========== Списки табелей ==============

def tabels(request):
 #Проверка на аутентификацию
    if request.user.is_authenticated:
        # Переменные
        type = TabelType.objects.all()
        group = Group.objects.get(name__icontains='Табельщик')
        tab_users = group.user_set.all().order_by('first_name')
        sq_period_month = request.GET.get('search_month', '')
        sq_period_year = request.GET.get('search_year', '')
        sq_dep = request.GET.get('t_tab_dep_search', '')
        sq_check = request.GET.get('tab_supcheck','')
        sq_user = request.GET.get('tab_user','')
        sq_this_month = request.GET.get('this_month','')
        sq_check_this_month = request.GET.get('chk_this_month','')
        sq_type = request.GET.get('search_type', '')
        user_ = request.user
        u_group = user_.groups.all()
        is_ro = 0
        # granted = 0
        unite = False
        is_atc = False
        answers = len(FeedBack.objects.filter(mes_from_id=request.user.id).filter(~Q(answer=None)).filter(~Q(answer='')).filter(answer_readed=0))

        # Права полтзователя
        Rights = get_rights(request)

        # Определение текущего месяца и года
        now = datetime.datetime.now()
        if len(str(now.month)) == 1:
            month_ = str(0) + str(now.month)
        else:
            month_ = now.month
        year_ = now.year

        # Проверка на права пользователя
        # for group in u_group:
        #     if (group.name == 'Сотрудник СУП') or (group.name == 'Сотрудник РО'):
        #         granted = True

        # if request.user.is_superuser:
        #     granted = True


        # Сообщения
        # Полный доступ
        # meslist = []
        # messages = InfoMessages.objects.filter(viewin=1).filter(active=1).order_by('-important','-id')
        # if Rights['granted'] == True:
        #     # Проверяем на постоянные и непостояннные
        #     for mes in messages:
        #         if mes.always:
        #             meslist.append(mes.id)
        #         else:
        #             if mes.dfrom <= datetime.datetime.now().date() and mes.dfrom >= datetime.datetime.now().date():
        #                 meslist.append(mes.id)
        #     messages = messages.filter(id__in=meslist)

        # else:
        #     deps = Department.objects.all().filter(user=user_.id)
        #     allow_departments = []
        #     for dep in deps:
        #         allow_departments.append(dep.id)
        #     for mes in messages:
        #         if mes.alldeps:
        #             meslist.append(mes.id)
        #         else:
        #             if mes.deps.filter(id__in=allow_departments):
        #                 meslist.append(mes.id)
        #     messages = messages.filter(id__in=meslist)



        if (Rights['granted'] == False):
            # если пользователь только с правами на определенные подразделения, собираем их тут:
            deps = Department.objects.all().filter(user=user_.id)
            allow_departments = []
            for dep in deps:

                allow_departments.append(dep.id)
                # если совмещение, то выдаем список автотранспорта
                if (dep.id == 3) or (dep.id == 2) or (dep.id == 26) or (dep.id == 40):
                    unite = True

                if (dep.id == 3) or (dep.id == 2):
                    is_atc = True
        if Rights['granted'] or Rights['payment_department']:
            deps = Department.objects.all().order_by('name')



        return render(request, 'TURV/tabels.html', context={'answers':      answers,
                                                             'type':        type,
                                                             'tab_users':   tab_users,
                                                             'deps':        deps,
                                                             'granted':     Rights['granted'],
                                                             'ro':          is_ro,
                                                             'month_':      month_,
                                                             "year_":       year_,
                                                             'unite':       unite,
                                                             'is_atc':      is_atc
                                                            #  'messages':    messages
                                                             })
    else:
        return redirect('/accounts/login/')

@login_required
def tabels_new(request):
    if request.user.is_authenticated:
            # Права полтзователя
        Rights = get_rights(request)
    else:
        return redirect('/accounts/login/')        

        # Переменные
    type = TabelType.objects.all()
    group = Group.objects.get(name__icontains='Табельщик')
    tab_users = group.user_set.all().order_by('first_name')
    
    sq_period_month = request.GET.get('search_month', '')
    sq_period_year = request.GET.get('search_year', '')
    sq_dep = request.GET.get('t_tab_dep_search', '')
    sq_check = request.GET.get('tab_supcheck','')
    sq_user = request.GET.get('tab_user','')
    sq_this_month = request.GET.get('this_month','')
    sq_check_this_month = request.GET.get('chk_this_month','')
    sq_type = request.GET.get('search_type', '')
    
    user_ = request.user
    u_group = user_.groups.all()
    is_ro = 0
    granted = 0
    unite = False
    is_atc = False
    answers = len(FeedBack.objects.filter(mes_from_id=request.user.id).filter(~Q(answer=None)).filter(~Q(answer='')).filter(answer_readed=0))

        # Определение текущего месяца и года
    now = datetime.datetime.now()
    if len(str(now.month)) == 1:
        month_ = str(0) + str(now.month)
    else:
        month_ = now.month
    year_ = now.year

    # # Проверка на права пользователя
    # for group in u_group:
    #     if (group.name == 'Сотрудник СУП') or (group.name == 'Сотрудник РО'):
    #         granted = True

    # if request.user.is_superuser:
    #     granted = True


    # # Сообщения
    # # Полный доступ
    # meslist = []
    # messages = InfoMessages.objects.filter(viewin=1).filter(active=1).order_by('-important','-id')
    # if granted == True:
    #     # Проверяем на постоянные и непостояннные
    #     for mes in messages:
    #         if mes.always:
    #             meslist.append(mes.id)
    #         else:
    #             if mes.dfrom <= datetime.datetime.now().date() and mes.dfrom >= datetime.datetime.now().date():
    #                 meslist.append(mes.id)
    #     messages = messages.filter(id__in=meslist)

    # else:
    #     deps = Department.objects.all().filter(user=user_.id).filter(is_aup=0)
    #     allow_departments = []
    #     for dep in deps:
    #         allow_departments.append(dep.id)
    #     for mes in messages:
    #         if mes.alldeps:
    #             meslist.append(mes.id)
    #         else:
    #             if mes.deps.filter(id__in=allow_departments):
    #                 meslist.append(mes.id)
    #     messages = messages.filter(id__in=meslist)



    if Rights['granted'] == False:
        # если пользователь только с правами на определенные подразделения, собираем их тут:
        deps = Department.objects.all().filter(user=user_.id).filter(is_aup=0)
        allow_departments = []
        for dep in deps:

            allow_departments.append(dep.id)
            # если совмещение, то выдаем список автотранспорта
            if (dep.id == 3) or (dep.id == 2) or (dep.id == 26) or (dep.id == 40):
                unite = True

            if (dep.id == 3) or (dep.id == 2):
                is_atc = True
    if Rights['granted'] or Rights['payment_department']:
        deps = Department.objects.all().order_by('name').filter(is_aup=0)

    # Определяем, какой интерфейс будет открыт
    if Rights['payment_department']:       
        InterfaceTemplate = 'TURV/tabels_payment.html'
    else:
        InterfaceTemplate = 'TURV/tabels.html'



    return render(request, InterfaceTemplate, context={'answers':answers,
                                                            'type':type,
                                                            'tab_users':tab_users,
                                                            'deps':deps,
                                                            'granted':Rights['granted'],
                                                            'ro':is_ro,
                                                            'month_':month_,
                                                            "year_":year_,
                                                            'unite':unite,
                                                            'is_atc':is_atc
                                                            })




# =========================================А

def tabels_json(request, type, year):

    Rights = get_rights(request)

    if year != 0:
        year = year
    else:
        year = str(DT.datetime.now().year)
    if type == 0:
        if Rights['granted'] == False:
            deps = Department.objects.filter(user=request.user.id)
            tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(iscorr=0).filter(department_id__in=deps).filter(type=1).filter(year=year).order_by('-year', '-month', 'department__name', 'id')
        if Rights['granted'] or Rights['payment_department']:
             tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(iscorr=0).filter(type=1).filter(year=year).order_by('-year', '-month', 'department__name', 'id')
            # tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(iscorr=0).filter(type=1).order_by('-year', '-month', 'department__name', 'id')
    else:
        if type == 10:
            if Rights['granted'] == False:
                deps = Department.objects.filter(user=request.user.id)
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr','half_month_check').filter(iscorr=1).filter(year=year).filter(department_id__in=deps).order_by('-year', '-month', 'department__name', 'id')
            if Rights['granted'] or Rights['payment_department']:
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr','half_month_check').filter(iscorr=1).filter(year=year).order_by('-year', '-month', 'department__name', 'id')
        else:
            if Rights['granted'] == False:
                deps = Department.objects.filter(user=request.user.id)
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr','half_month_check').filter(iscorr=0).filter(year=year).filter(department_id__in=deps).filter(type=type).order_by('-year', '-month', 'department__name', 'id')
            if Rights['granted'] or Rights['payment_department']:
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr','half_month_check').filter(iscorr=0).filter(year=year).filter(type=type).order_by('-year', '-month', 'department__name', 'id')

    tabels = list(tabels)
    return JsonResponse(tabels, safe=False)


# ====================================================

def tabels_json_multi(request, type, month, year, dep, half_month):
    if len(str(month)) != 2:
        month = '0'+ str(month)
    else:
        month = month

    if type == 2:
        items = TabelItem.objects.values('bound_tabel_id','employer__fullname', 'toxic_p', 'w_hours').filter(year=year).filter(month=month).filter(bound_tabel__department_id=dep).filter(bound_tabel__type_id=2).filter(bound_tabel__sup_check=1).order_by('employer__fullname')

    if type == 3:
        items = TabelItem.objects.values('bound_tabel_id','employer__fullname', 'auto__unite_p', 'employer__stand_worktime', 'w_hours', 'employer__positionOfPayment').filter(year=year).filter(month=month).filter(bound_tabel__department_id=dep).filter(bound_tabel__type_id=3).filter(bound_tabel__sup_check=1).order_by('employer__fullname')

    if type == 9:
        items_main = TabelItem.objects.values('bound_tabel_id','employer__fullname', 'w_hours').filter(year=year).filter(month=month).filter(employer__department_id=dep).filter(bound_tabel__type_id=9).filter(bound_tabel__del_check=0).order_by('employer__fullname')
        items_sub = TabelItem.objects.values('bound_tabel_id','employer__fullname', 'w_hours').filter(year=year).filter(month=month).filter(employer__aup_id=dep).filter(bound_tabel__type_id=9).filter(bound_tabel__del_check=0).order_by('employer__fullname')
        items = items_main.union(items_sub).values('bound_tabel_id','employer__fullname', 'w_hours').order_by('employer__fullname')
    if type == 1:
        if half_month == 0:
            items = TabelItem.objects.values('employer__fullname','employer__position__name','hours1','hours2','hours3','hours4','hours5','hours6','hours7','hours8','hours9','hours10','hours11','hours12','hours13','hours14','hours15','hours16','hours17','hours18','hours19', 'hours20','hours21','hours22','hours23','hours24','hours25','hours26','hours27','hours28','hours29','hours30','hours31','type_time1','type_time2','type_time3','type_time4','type_time5','type_time6','type_time7','type_time8','type_time9','type_time10','type_time11','type_time12','type_time13','type_time14','type_time15','type_time16','type_time17','type_time18','type_time19','type_time20','type_time21','type_time22','type_time23','type_time24','type_time25','type_time26','type_time27','type_time28','type_time29','type_time30','type_time31', 'bound_tabel_id').filter(bound_tabel__year=year).filter(bound_tabel__month=month).filter(bound_tabel__department_id=dep).filter(bound_tabel__type_id=1).filter(bound_tabel__del_check=0).filter(bound_tabel__sup_check=1).order_by('employer__fullname')
        if half_month == 1:
            items = TabelItem.objects.values('employer__fullname','employer__position__name','hours1','hours2','hours3','hours4','hours5','hours6','hours7','hours8','hours9','hours10','hours11','hours12','hours13','hours14','hours15','hours16','hours17','hours18','hours19', 'hours20','hours21','hours22','hours23','hours24','hours25','hours26','hours27','hours28','hours29','hours30','hours31','type_time1','type_time2','type_time3','type_time4','type_time5','type_time6','type_time7','type_time8','type_time9','type_time10','type_time11','type_time12','type_time13','type_time14','type_time15','type_time16','type_time17','type_time18','type_time19','type_time20','type_time21','type_time22','type_time23','type_time24','type_time25','type_time26','type_time27','type_time28','type_time29','type_time30','type_time31', 'bound_tabel_id').filter(bound_tabel__year=year).filter(bound_tabel__month=month).filter(bound_tabel__department_id=dep).filter(bound_tabel__type_id=1).filter(bound_tabel__del_check=0).filter(bound_tabel__half_month_check=1).order_by('employer__fullname')


    items = list(items)
    return JsonResponse(items, safe=False)

def deps_json(request,type):


    if type == 2:
        deps = Department.objects.values('id', 'name', 'onescode').filter(notused=0).filter(is_aup=0)
    else:
    
        if type == 0:
            deps = Department.objects.values('id', 'name', 'onescode').filter(notused=0).filter(shift=1)
        else:
            deps = Department.objects.values('id', 'name', 'onescode').filter(notused=0).filter(conftype=type)
    deps = list(deps)
    return JsonResponse(deps, safe=False)

def tabel_unload_check(request,id):
    print(request.user)
    tabel = Tabel.objects.get(id=id)
    tabel.unloaded = True
    tabel.save()
    return redirect('/turv')

def tabel_half_month_check(request, id):
    if request.user.is_authenticated:
        tabel = Tabel.objects.get(id=id)
        if tabel.half_month_check == True:
            tabel.half_month_check = False
        else:

            tabel.half_month_check = True
        tabel.save()

        return redirect('/turv/create/' + str(id))


def tabels_json_search(request):
    Rights = get_rights(request)

    sq_period_month = request.GET.get('search_month', '')
    sq_period_year = request.GET.get('search_year', '')
    sq_dep = request.GET.get('t_tab_dep_search', '')
    sq_check = request.GET.get('tab_supcheck','')
    sq_user = request.GET.get('tab_user','')
    sq_this_month = request.GET.get('this_month','')
    sq_check_this_month = request.GET.get('chk_this_month','')
    sq_type = request.GET.get('search_type', '')
    sq_code = request.GET.get('search_code', '')

    # Алгоритм поиска
    if not Rights['granted']:
        allow_departments = Department.objects.filter(user=request.user.id)


        if (sq_period_month) and (sq_period_year) and (sq_type):
            if sq_type == 'c':
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(department_id__in=allow_departments).filter(year=sq_period_year).filter(del_check=0).filter(month=sq_period_month).filter(iscorr=1).order_by('-year', '-month', 'type__id')
            else:
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(department_id__in=allow_departments).filter(year=sq_period_year).filter(del_check=0).filter(month=sq_period_month).filter(type_id=sq_type).order_by('-year', '-month', 'type__id')
        else:
            if (sq_period_month) and (sq_period_year):
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(department_id__in=allow_departments).filter(year=sq_period_year).filter(del_check=0).filter(month=sq_period_month).order_by('-year', '-month', 'type__id')
            else:
                if (sq_period_month):
                    tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(department_id__in=allow_departments).filter(month=sq_period_month).filter(del_check=0).order_by('-year', '-month', 'type__id')
                else:
                    if (sq_period_year):
                        tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(department_id__in=allow_departments).filter(year=sq_period_year).filter(del_check=0).order_by('-year', '-month', 'type__id')
                    else:
                        if (sq_dep):
                            tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(department_id=sq_dep).filter(del_check=0).order_by('-year', '-month', 'type__id')
                        else:
                            if (sq_type):
                                if sq_type == 'c':
                                    tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(iscorr=1).filter(department_id__in=allow_departments).filter(del_check=0).order_by('-year', '-month', 'type__id')
                                else:
                                    tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(type_id=sq_type).filter(department_id__in=allow_departments).filter(del_check=0).order_by('-year', '-month', 'type__id')
                            else:
                                if (sq_code):
                                    tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(id=sq_code).order_by('-year', '-month',   'department__id' , 'type__id')
                                else:
                                    tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(~Q(type_id=8)).filter(day='0').order_by('-year', '-month',   'department__id' , 'type__id')



    if Rights['granted'] or Rights['payment_department']:
        # если у пользователя полные права, то выдаем все
        deps = Department.objects.all().order_by('name')
        # Алгоритм поиска
        pag = 1000
        if (sq_period_month) and (sq_period_year) and (sq_dep) and (sq_type):
            if sq_type == 'c':
                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).filter(month=sq_period_month).filter(department_id=sq_dep).filter(iscorr=1).order_by('-year', '-month',   'department__id' , 'type__id')
            else:

                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).filter(month=sq_period_month).filter(department_id=sq_dep).filter(type_id=sq_type).order_by('-year', '-month',   'department__id' , 'type__id')
        else:
            if (sq_period_month) and (sq_period_year) and (sq_dep):

                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).filter(month=sq_period_month).filter(department_id=sq_dep).order_by('-year', '-month',   'department__id' , 'type__id')
            else:
                if (sq_period_month) and (sq_period_year) and (sq_type):
                    if sq_type == 'c':
                        tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).filter(month=sq_period_month).filter(iscorr=1).order_by('-year', '-month',   'department__id' , 'type__id')
                    else:
                        tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).filter(month=sq_period_month).filter(type_id=sq_type).order_by('-year', '-month',   'department__id' , 'type__id')
                else:
                    if (sq_period_month) and (sq_period_year):

                        tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).filter(month=sq_period_month).filter(year=sq_period_year).filter(day='0').order_by('-year', '-month',   'department__id' , 'type__id')
                    else:

                            if (sq_period_year) and (sq_dep):
                                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).filter(department_id=sq_dep).order_by('-year', '-month',   'department__id' , 'type__id')
                            else:
                                if (sq_period_month):
                                    tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(month=sq_period_month).order_by('-year', '-month',   'department__id' , 'type__id')
                                else:
                                    if (sq_period_year):
                                        tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=sq_period_year).order_by('-year', '-month',   'department__id' , 'type__id')
                                    else:
                                        if (sq_dep):
                                            tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(department_id=sq_dep).filter(day='0').order_by('-year', '-month',   'department__id' , 'type__id')
                                        else:
                                            if (sq_this_month):
                                                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=year_).filter(month=month_).filter(day='0').order_by('-year', '-month',   'department__id' , 'type__id')
                                            else:
                                                if (sq_check_this_month):
                                                    tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(year=year_).filter(month=month_).filter(day='0').filter(sup_check= True).order_by('-year', '-month',   'department__id' , 'type__id')
                                                else:
                                                    if (sq_user):
                                                        tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(res_officer=sq_user).order_by('-year', '-month',   'department__id' , 'type__id')
                                                    else:
                                                        if (sq_type):
                                                            if sq_type == 'c':
                                                                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(iscorr=1).order_by('-year', '-month',   'department__id' , 'type__id')
                                                            else:
                                                                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(type_id=sq_type).order_by('-year', '-month',   'department__id' , 'type__id')
                                                        else:
                                                            if (sq_code):
                                                                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(id=sq_code).order_by('-year', '-month',   'department__id' , 'type__id')
                                                            else:
                                                                tabels = Tabel.objects.values('id', 'month', 'year', 'type__name', 'department', 'department__name', 'del_check', 'sup_check', 'paper_check', 'unloaded', 'res_officer', 'comm', 'iscorr', 'half_month_check').filter(~Q(type_id=8)).filter(day='0').order_by('-year', '-month',   'department__id' , 'type__id')

    tabels = list(tabels)
    return JsonResponse(tabels, safe=False)


def over_tabels(request, type):
 #Проверка на аутентификацию
    if request.user.is_authenticated:
        # Переменные
        type        = TabelType.objects.get(id=type)
        group       = Group.objects.get(name__icontains='Табельщик')
        tab_users   = group.user_set.all().order_by('first_name')
        user_       = request.user
        u_group     = user_.groups.all()
        is_ro       = 0
        granted     = 0
        unite       = False

        # Проверка на права пользователя
        for group in u_group:
            if (group.name == 'Сотрудник СУП') or (group.name == 'Сотрудник РО'):
                granted = True

        if request.user.is_superuser:
            granted = True
            unite = True

        if (granted == False):
            # если пользователь только с правами на определенные подразделения, собираем их тут:
            deps = Department.objects.all().filter(user=user_.id)
        else:
            deps = Department.objects.all()

        if granted == 1:
            pag = 40
            tabels = Tabel.objects.all().filter(type=type).filter(department_id__in=(2,3)).order_by('-year', '-month', '-day', 'type__id')
        else:
            pag = 40
            tabels = Tabel.objects.all().filter(type=type).filter(department__in=list(deps)).order_by('-year', '-month', '-day', 'type__id')
        p_tabels = Paginator(tabels, pag)
        page_number = request.GET.get('page', 1)
        page = p_tabels.get_page(page_number)
        count = len(tabels)



        return render(request, 'TURV/over-tabels.html', context={'type':type, 'tab_users':tab_users, 'tabels':page, 'count':count, 'deps':deps, 'granted':granted, 'ro':is_ro, 'unite':unite})
    else:
        return redirect('/accounts/login/')

def tabels_forload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            year = request.POST.get('fl-year', '')
            month = request.POST.get('fl-month',  '')
            half = request.POST.get('fl-half','')

            if half:
                tabels = Tabel.objects.filter(month=str(month)).filter(year=str(year)).filter(type_id=1).filter(del_check=0).filter(sup_check=0).filter(iscorr=0).filter(unloaded=0).filter(half_month_check=1).order_by('department__name')
            else:
                tabels = Tabel.objects.filter(month=str(month)).filter(year=str(year)).filter(type_id=1).filter(del_check=0).filter(sup_check=1).filter(iscorr=0).filter(department__shift=1).filter(unloaded=0).order_by('department__name')
        # tabels = Tabel.objects.all()
            return render(request, 'TURV/for-load.html', context={'tabels':tabels, 'count':len(tabels)})
        else:
            year =  datetime.date.today().year

            month = datetime.date.today().month
            if len(str(month)) == 1:
                month = '0' + str(month)
            else:
                month = month

            tabels = Tabel.objects.filter(month=month).filter(year=year).filter(type_id=1).filter(del_check=0).filter(sup_check=1).filter(iscorr=0).filter(department__shift=1).filter(unloaded=0).order_by('department__name')
            # tabels = Tabel.objects.all()
            print(tabels)
            return render(request, 'TURV/for-load.html', context={'tabels':tabels, 'count':len(tabels)})


# =========================================


 #Проверка на аутентификацию
    if request.user.is_authenticated:
        # Переменные
        type = TabelType.objects.all()
        group = Group.objects.get(name__icontains='Табельщик')
        tab_users = group.user_set.all().order_by('first_name')
        sq_period_month = request.GET.get('search_month', '')
        sq_period_year = request.GET.get('search_year', '')
        sq_dep = request.GET.get('t_tab_dep_search', '')
        sq_check = request.GET.get('tab_supcheck','')
        sq_user = request.GET.get('tab_user','')
        sq_this_month = request.GET.get('this_month','')
        sq_check_this_month = request.GET.get('chk_this_month','')
        sq_type = request.GET.get('search_type', '')
        user_ = request.user
        u_group = user_.groups.all()
        is_ro = 0
        granted = 0
        unite = False

        # Определение текущего месяца и года
        now = datetime.datetime.now()
        if len(str(now.month)) == 1:
            month_ = str(0) + str(now.month)
        else:
            month_ = now.month
        year_ = now.year

        # Проверка на права пользователя
        for group in u_group:
            if (group.name == 'Сотрудник СУП') or (group.name == 'Сотрудник РО'):
                granted = True

        if request.user.is_superuser:
            granted = True
            unite = True

        if (granted == False):
            # если пользователь только с правами на определенные подразделения, собираем их тут:
            deps = Department.objects.all().filter(user=user_.id)
            allow_departments = []
            for dep in deps:

                allow_departments.append(dep.id)
                # если атц, то выдаем список автотранспорта
                if (dep.id == 3) or (dep.id == 2) :

                    print(unite)
                    unite = True


        else:
            deps = Department.objects.all()

        if granted == 1:
            pag = 40
            tabels = Tabel.objects.all().filter(type_id=8).filter(department_id__in=(2,3)).order_by('-year', '-month', '-day', 'type__id')
        else:
            pag = 40
            tabels = Tabel.objects.all().filter(type_id=8).filter(department_id__in=allow_departments).order_by('-year', '-month', '-day', 'type__id')

        p_tabels = Paginator(tabels, pag)
        page_number = request.GET.get('page', 1)
        page = p_tabels.get_page(page_number)
        count = len(tabels)



        return render(request, 'TURV/nn-tabels.html', context={'type':type, 'tab_users':tab_users, 'tabels':page, 'count':count, 'deps':deps, 'granted':granted, 'ro':is_ro, 'month_':month_, "year_":year_, 'unite':unite})
    else:
        return redirect('/accounts/login/')

# =========================================

# ========== Основные функции =============

def tabel_create(request, id):
    Rights = get_rights(request)
    
    sq_employer = request.GET.get('its_employer','')
    sq_position = request.GET.get('its_position','')
    user_ = request.user
    b_tabel = Tabel.objects.get(id=id)
    if request.method == "GET":
            
            c_tabels = Tabel.objects.filter(iscorr=1).filter(corr_id=id).filter(sup_check=1).order_by('-id').filter(type_id=1)

            # Корректировка. Эту хрень надо переписать
            if c_tabels:
                corr_emps = []
                corr_items = []
                for c in c_tabels:
                    if len(c_tabels) == 1:
                        c_items = TabelItem.objects.all().filter(bound_tabel_id=c.id)
                        for item in c_items:
                            corr_emps.append(str(item.employer_id))
                        items = TabelItem.objects.filter(~Q(employer_id__in=corr_emps)).filter(bound_tabel=id)
                        corr_items = []
                        for i in items:
                            corr_items.append(i.id)
                        for i in c_items:
                            corr_items.append(i.id)
                        items = TabelItem.objects.filter(id__in=corr_items).order_by('employer')
                    else:
                        corr_emps = []
                        corr_items = []
                        corr_tabels = []
                        for c_tabel in c_tabels:
                            corr_tabels.append(c_tabel.id)
                        c_items = TabelItem.objects.filter(bound_tabel_id__in=corr_tabels).order_by('-bound_tabel_id')
                        for item in c_items:
                            c_emps = c_items.filter(employer_id=item.employer_id)
                            if len(c_emps) == 1:
                                corr_emps.append(item.employer_id)
                                corr_items.append(item.id)
                            else:
                                last = c_emps.latest('id')
                                corr_emps.append(last.employer_id)
                                corr_items.append(last.id)
                        items = TabelItem.objects.filter(~Q(employer_id__in=corr_emps)).filter(bound_tabel_id=id)
                        for i in items:
                            corr_items.append(i.id)
                        items = TabelItem.objects.filter(id__in=corr_items).order_by('employer')
                # =========================================
            else:
                if request.GET.get('search-sign', '') == '1':
                    search_query = {
                        'tabel_id': b_tabel.id,
                        'name': request.GET.get('tabel-create-search-name', ''),
                        'position': request.GET.get('tabel-create-search-position', '') 
                    }

                    items = search_tabel_item(search_query)    
                else:
                    items = TabelItem.objects.filter(bound_tabel=id).order_by('employer')


    

    # ----------------------------


            tabel_form = Tabel_form(instance=b_tabel)



            if (b_tabel.type_id != 1) or (b_tabel.type_id == 4) or (b_tabel.type_id == 5) or (b_tabel.type_id == 6):
                hours = items.aggregate(sum_of_hours=Sum("w_hours"), sum_of_lhours=Sum("sHours19"), sum_of_days=Sum("w_days"),  s_over=Sum('sHours4'), s_night=Sum("sHours2"), s_vacwork=Sum("sHours3"),     s_vac=Sum("v_days"), s_weekends=Sum("sHours24"))
                s_hours = hours['sum_of_hours']
                s_lhours = hours['sum_of_lhours']
                s_days = hours['sum_of_days']
                s_over = hours['s_over']
                s_night = hours['s_night']
                s_vacwork = hours['s_vacwork']
                s_vac = hours['s_vac']
                s_weekends = hours['s_weekends']
            else:
                hours = items.aggregate(sum_of_hours=Sum("w_hours"), sum_of_lhours=Sum("sHours19"), sum_of_days=Sum("w_days"),  s_over=Sum('sHours4'), s_night=Sum("sHours2"), s_vacwork=Sum("sHours3"),     s_vac=Sum("v_days"), s_weekends=Sum("sHours24")/8)
                s_hours = hours['sum_of_hours']
                s_lhours = hours['sum_of_lhours']
                s_days = hours['sum_of_days']
                s_over = hours['s_over']
                s_night = hours['s_night']
                s_vacwork = hours['s_vacwork']
                s_vac = hours['s_vac']
                s_weekends = hours['s_weekends']

            # # Сообщения
            # # Полный доступ
            # meslist = []
            # messages = InfoMessages.objects.filter(viewin=2).filter(active=1).order_by('-important','-id')
            # if granted == True:
            #     # Проверяем на пренадлежность к виду табеля
            #     for mes in messages:
            #         if mes.alltypes:
            #             meslist.append(mes.id)
            #         else:
            #             if mes.intypes.filter(id=b_tabel.type_id):
            #                 meslist.append(mes.id)

            #     messages = messages.filter(id__in=meslist)
            #     meslist = []
                
            #     # Сортировка по периодам
            #     for mes in messages:
            #         if mes.always:
            #             meslist.append(mes.id)
            #         else:
            #             if mes.dfrom <= datetime.datetime.now().date() and mes.dfrom >= datetime.datetime.now().date():
            #                 meslist.append(mes.id)


            #     messages = messages.filter(id__in=meslist)
            #     meslist = []
                

            #     # Сортировка по подразделениям
            #     for mes in messages:
            #         if  mes.alldeps:
            #             meslist.append(mes.id)
            #         else:
            #             if mes.deps.filter(id=b_tabel.department_id):
            #                 meslist.append(mes.id)

            #             messages = messages.filter(id__in=meslist)

                

            # #неполный доступ
            # else:
            #     deps = Department.objects.all().filter(user=user_.id)
            #     allow_departments = []
            #     for dep in deps:
            #         allow_departments.append(dep.id)
            #     for mes in messages:
            #         if mes.alldeps:
            #             meslist.append(mes.id)
            #         else:
            #             if mes.deps.filter(id=b_tabel.department_id):
            #                 meslist.append(mes.id)
            #     messages = messages.filter(id__in=meslist)



            count = len(items)
            t_month = b_tabel.month
            t_year = b_tabel.year
            t_dep = b_tabel.department
            if (b_tabel.type_id != 1) and (b_tabel.type_id != 4) and (b_tabel.type_id != 5):

                return render(request, 'TURV/create_tabel_small.html', context={        's_hours':              s_hours,
                                                                                        's_lhours':             s_lhours,
                                                                                        's_days':               s_days,
                                                                                        's_over':               s_over,
                                                                                        's_night':              s_night,
                                                                                        's_vacwork':            s_vacwork,
                                                                                        's_vac':                s_vac,
                                                                                        's_weekends':           s_weekends,
                                                                                        'hours':                hours,
                                                                                        'form':                 tabel_form,
                                                                                        'items':                items,
                                                                                        'month':                t_month,
                                                                                        'year':                 t_year,
                                                                                        'count':                count,
                                                                                        'b_tabel':              b_tabel,
                                                                                        'granted':              Rights['granted'],
                                                                                        'IsPaymentDepartment':  Rights['payment_department']})
            else:

                return render(request, 'TURV/create_tabel.html', context={
                                                                            's_hours':              s_hours,
                                                                            's_lhours':             s_lhours,
                                                                            's_days':               s_days,
                                                                            's_over':               s_over,
                                                                            's_night':              s_night,
                                                                            's_vacwork':            s_vacwork,
                                                                            's_vac':                s_vac,
                                                                            's_weekends':           s_weekends,
                                                                            'hours':                hours,
                                                                            'form':                 tabel_form, 
                                                                            'items':                items,
                                                                            'month':                t_month,
                                                                            'year':                 t_year,
                                                                            'count':                count,
                                                                            'b_tabel':              b_tabel,
                                                                            'granted':              Rights['granted'],
                                                                            'IsPaymentDepartment':  Rights['payment_department']
                                                                            })

    else:

            b_tabel = Tabel.objects.get(id=id)
            bound_form = Tabel_form(request.POST, instance=b_tabel)
            if bound_form.is_valid():

                bound_form.save()
                return render(request, 'TURV/close.html')


# Добавление комментария к табелю

def upd_comm(request,id):
    if request.user.is_authenticated:

        comm = request.POST.get('tabel_comm','')
        tabel = Tabel.objects.get(id=id)
        print(comm)
        tabel.comm = comm
        tabel.save()
        return redirect('/turv/create/' + str(id))

# ===============================

# Создание нового табеля

def new_tabel(request):
    if request.user.is_authenticated:
        Rights = get_rights(request)
    else:
        return render(request, 'reg_jounals/no_auth.html')
        
    user_ = request.user

    if Rights['granted'] or Rights['payment_department']:
        deps = Department.objects.filter(is_aup=0)
    else:
        deps = Department.objects.filter(user=user_.id)
    tabel_form = Tabel_form()
    
    if request.method == "POST":
        tabel_form = Tabel_form(request.POST)
        if tabel_form.is_valid():
            user_ = request.user.first_name
            tabel_form.saveFirst(user_)
            last_tabel = Tabel.objects.latest('id')
        else:
            error_tabel = tabel_form.errors.as_text().split('*')[2]

            return render(request, 'TURV/new_tabel.html', context={'form':tabel_form, 'deps':deps, 'error_tabel':error_tabel})
        if last_tabel.department_id == 2 or last_tabel.department_id == 3 or last_tabel.department_id == 26 or last_tabel.department_id == 40:
            if last_tabel.type_id == 4:
                return redirect('/turv/over/4')
            else:
                if last_tabel.type_id == 5:
                    return redirect('/turv/over/5')
                else:
                    if last_tabel.type_id == 8:
                        return redirect('/turv/over/8')
                    else:
                        return redirect('..')
        else:
            return redirect('..')

    else:

        return render(request, 'TURV/new_tabel.html', context={'form':tabel_form, 'deps':deps})


# ===============================

# Создание корректирующего табеля

def new_corr_tabel(request, id):
    if request.user.is_authenticated:
        tabel = Tabel.objects.get(id=id)
        if tabel:
            new_corr = Tabel.objects.create(
                year = tabel.year,
                month = tabel.month,
                department = tabel.department,
                type = tabel.type,
                day = tabel.day,
                iscorr = True,
                corr = tabel,
                res_officer = tabel.res_officer,
                comm = 'Корр. ' + str(tabel.month) + ' ' + str(tabel.year)

            )

            new_corr.save()

            last_corr = Tabel.objects.all().filter(iscorr=True).latest('id')

            return redirect('/turv/create/' + str(last_corr.id))

# ================================

# ====== Действия с табелем ==================

def tabel_delcheck(request,id):
    if request.user.is_authenticated:
        tabel = Tabel.objects.get(id=id)
        print(tabel.del_check)
        if tabel.del_check == True:
            tabel.del_check = False
            tabel.save()
        else:
            tabel.del_check = True
            tabel.save()
        return redirect('/turv/create/' + str(id))

def del_tabel(request):
    if request.user.is_authenticated:
        for_delete = Tabel.objects.filter(del_check = True)
        for tabel in for_delete:
            print(tabel)
            items_for_delete = TabelItem.objects.filter(bound_tabel=tabel.id)
            for item in items_for_delete:
                print(item)
                item.delete()
            tabel.delete()
    return redirect('/turv')

def tabel_additem(request, id):
    if request.user.is_authenticated:
        b_tabel = Tabel.objects.get(id=id)
        in_tabel_items = TabelItem.objects.filter(bound_tabel=id).order_by('-id')
        year = b_tabel.year
        month = b_tabel.month
        department = b_tabel.department
        user_ = request.user
        allow_employers = Employers.objects.filter(department_id=department).filter(fired=0)
        granted = access_check(request)

        # Сообщения
        # Полный доступ
        meslist = []
        messages = InfoMessages.objects.filter(viewin=3).filter(active=1).order_by('-important','-id')
        if granted == True:
            # Проверяем на пренадлежность к виду табеля
            for mes in messages:
                if mes.alltypes:
                    meslist.append(mes.id)
                else:
                    if mes.intypes.filter(id=b_tabel.type_id):
                        meslist.append(mes.id)

            messages = messages.filter(id__in=meslist)
            meslist = []

            for mes in messages:
                if mes.always:
                    meslist.append(mes.id)
                else:
                    if mes.dfrom <= datetime.datetime.now().date() and mes.dfrom >= datetime.datetime.now().date():
                        meslist.append(mes.id)


            messages = messages.filter(id__in=meslist)
            meslist = []

            for mes in messages:
                if  mes.alldeps:
                    pass
                else:
                    if mes.deps.filter(id=department.id):
                        meslist.append(mes.id)

                    messages = messages.filter(id__in=meslist)


        #неполный доступ
        else:

            for mes in messages:
                if mes.alltypes:
                    meslist.append(mes.id)
                else:
                    if mes.intypes.filter(id=b_tabel.type_id):
                        meslist.append(mes.id)

            messages = messages.filter(id__in=meslist)
            meslist = []


            deps = Department.objects.all().filter(user=user_.id)
            allow_departments = []
            for dep in deps:
                allow_departments.append(dep.id)


            for mes in messages:
                if mes.alldeps:
                    meslist.append(mes.id)
                else:
                    if mes.deps.filter(id=department.id):
                        meslist.append(mes.id)
            messages = messages.filter(id__in=meslist)






        tabelItem_form = TabelItem_form()

        if request.method == "POST":
            tabelItem_form = TabelItem_form(request.POST)
            if tabelItem_form.is_valid():
                user_ = request.user.first_name
                tabelItem_form.saveFirst(id)
                loc = '/turv/additem/'+str(id)
                return redirect(loc)
        else:
            tabelItem_form.fields['employer'].queryset  = allow_employers
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'TURV/new_tabel_item.html', context={'tabel':tabelItem_form, 'in_tabel':in_tabel_items, 'b_tabel':b_tabel, 'year':year, 'month':month, 'emps':allow_employers, 'messages':messages})

def tabel_upditem(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":

            item = TabelItem.objects.get(id=id)

            bound_form = TabelItem_form(instance=item)
            year = item.bound_tabel.year
            month = item.bound_tabel.month
            department = item.bound_tabel.department
            type = item.bound_tabel.type_id
            bound_form.fields['employer'].queryset = Employers.objects.filter(department=item.bound_tabel.department)
            if type != 1 and type != 4 and type != 5 and type != 6:
                return render(request, 'TURV/upd_tabel_itemSmall.html', context={'tabel':bound_form, 'item':item, 'b_tabel':item.bound_tabel.id, 'year':year, 'month':month, 'type':type})
            else:
                return render(request, 'TURV/upd_tabel_item.html', context={'tabel':bound_form, 'item':item, 'b_tabel':item.bound_tabel.id, 'year':year, 'month':month, 'type':type})

        else:
            item = TabelItem.objects.get(id=id)
            tabelItem_form = TabelItem_form(request.POST, instance=item)
            if tabelItem_form.is_valid():


                tabelItem_form.save()
                loc = '/turv/create/'+str(item.bound_tabel.id)
                return redirect(loc)

    else:
        return render(request, 'reg_jounals/no_auth.html')

def tabel_paper_check(request, id):
    if request.user.is_authenticated:
            tabel = Tabel.objects.get(id=id)

            if tabel.paper_check == False:
                tabel.paper_check = True
            else:
                tabel.paper_check = False

            tabel.save()

    return redirect('/turv/create/' + str(id))

def tabel_sup_check(request, id):
    if request.user.is_authenticated:
            tabel = Tabel.objects.get(id=id)

            if tabel.sup_check == False:
                tabel.sup_check = True
                logs.objects.create(
                    date = DT.datetime.now(),
                    event = logs_event.objects.get(id=4),
                    doc_id = id,
                    type = 'Табель проверен',
                    number = id,
                    year = tabel.year,
                    doc_date = DT.datetime.strptime(str(tabel.year + '-' + tabel.month + '-' + str(DT.datetime.now().day)), '%Y-%M-%d'),
                    addData = 'Табель ' + str(tabel.type.name) + ' ' + str(tabel.department.name) + ' ' + str(tabel.year) + ' ' + str(tabel.month) + ' проверен сотрудником СУП' ,
                    link = '/turv/create/' + str(id),
                    res_officer = request.user.first_name)

            else:
                tabel.sup_check = False

            tabel.save()

    return redirect('/turv/create/' + str(id))

def tabel_delitem(request, id):


    if request.user.is_authenticated:
        item = TabelItem.objects.get(id__iexact=id)
        num = item.bound_tabel.id
        dest = '/turv/create/' + str(num)
        item.delete()
        return redirect(dest)

@login_required
def tabel_getitem(request, emp, tab):
    this_tabel = Tabel.objects.get(id=tab)
    main_tabel = Tabel.objects.get(id=this_tabel.corr_id)
    items = TabelItem.objects.filter(bound_tabel=main_tabel.id).filter(employer=emp)
    item = items[0]
    table = list()
    table.append({
        'id':item.id,
        'tt1':item.type_time1,
        'tt2':item.type_time2,
        'tt3':item.type_time3,
        'tt4':item.type_time4,
        'tt5':item.type_time5,
        'tt6':item.type_time6,
        'tt7':item.type_time7,
        'tt8':item.type_time8,
        'tt9':item.type_time9,
        'tt10':item.type_time10,
        'tt11':item.type_time11,
        'tt12':item.type_time12,
        'tt13':item.type_time13,
        'tt14':item.type_time14,
        'tt15':item.type_time15,
        'tt16':item.type_time16,
        'tt17':item.type_time17,
        'tt18':item.type_time18,
        'tt19':item.type_time19,
        'tt20':item.type_time20,
        'tt21':item.type_time21,
        'tt22':item.type_time22,
        'tt23':item.type_time23,
        'tt24':item.type_time24,
        'tt25':item.type_time25,
        'tt26':item.type_time26,
        'tt27':item.type_time27,
        'tt28':item.type_time28,
        'tt29':item.type_time29,
        'tt30':item.type_time30,
        'tt31':item.type_time31,
        'h1':item.hours1,
        'h2':item.hours2,
        'h3':item.hours3,
        'h4':item.hours4,
        'h5':item.hours5,
        'h6':item.hours6,
        'h7':item.hours7,
        'h8':item.hours8,
        'h9':item.hours9,
        'h10':item.hours10,
        'h11':item.hours11,
        'h12':item.hours12,
        'h13':item.hours13,
        'h14':item.hours14,
        'h15':item.hours15,
        'h16':item.hours16,
        'h17':item.hours17,
        'h18':item.hours18,
        'h19':item.hours19,
        'h20':item.hours20,
        'h21':item.hours21,
        'h22':item.hours22,
        'h23':item.hours23,
        'h24':item.hours24,
        'h25':item.hours25,
        'h26':item.hours26,
        'h27':item.hours27,
        'h28':item.hours28,
        'h29':item.hours29,
        'h30':item.hours30,
        'h31':item.hours31,
        'wdays':item.w_days,
        'whours':item.w_hours,
        'vdays':item.v_days,
        'vhours':item.v_hours
    })
    return JsonResponse(table, safe=False)
# =============================================

# Справочники ---------------------------------

def messages_ref(request):
    if request.user.is_authenticated:
        messages = InfoMessages.objects.all()
        return render(request, 'TURV/messages.html', context={'messages':messages})

def new_message(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            if id != 0:
                message = InfoMessages.objects.get(id=id)
                form = InfoMessages_form(instance=message)
            else:
                form = InfoMessages_form()

            return render(request, 'TURV/message-form.html', context={'form':form})
        else:
            if id == 0:
                form = InfoMessages_form(request.POST)
                if form.is_valid():
                        form.saveFirst()
                        return redirect('/turv/messages/')
                else:
                    return render(request, 'TURV/message-form.html', context={'form':form})
            else:
                message = InfoMessages.objects.get(id=id)
                form = InfoMessages_form(request.POST, instance=message)
                if form.is_valid():
                    form.save()
                    return redirect('/turv/messages/')
                else:
                    return render(request, 'TURV/message-form.html', context={'form':form})

# ==================== Отзывы ==================

def feedbacks(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            unreaded = request.POST.get('unreaded_only', '')
            if unreaded:
                feedbacks = FeedBack.objects.filter(readed=0)
            else:
                feedbacks = FeedBack.objects.all()
        else:
            feedbacks = FeedBack.objects.filter(mes_from_id=request.user.id)
        p_emps = Paginator(feedbacks, 20)
        page_number = request.GET.get('page', 1)
        page = p_emps.get_page(page_number)
        return render(request, 'TURV/feedbacks.html', context={'feedbacks':page})
    else:
        return render(request, 'reg_jounals/no_auth.html')


def new_feedback(request, id):
    if request.user.is_authenticated:
        state = ''
        if request.method == 'GET':
            if id != 0:
                feedback = FeedBack.objects.get(id=id)
                state = 'upd'
                form = FeedBack_form(instance=feedback)
                return render(request, 'TURV/feedback-form.html', context={'form':form, 'feedback':feedback, 'state':state})
            else:
                form = FeedBack_form()
                return render(request, 'TURV/feedback-form.html', context={'form':form})
        else:
            if id == 0:
                form = FeedBack_form(request.POST)
                user_io = request.user.first_name
                user_io = user_io.split(' ')
                if len(user_io) < 3:
                    user_io = user_io[0]
                else:
                    user_io = user_io[1] + ' ' + user_io[2]
                if form.is_valid():
                    form.saveFirst(request.user.id)
                    return render(request, 'TURV/thankyou.html', context={'user_io':user_io})
                else:
                    return render(request, 'TURV/feedback-form.html', context={'form':form})
            else:
                feedback = FeedBack.objects.get(id=id)
                form = FeedBack_form(request.POST, instance=feedback)
                if form.is_valid():
                    form.save()
                    feedback = FeedBack.objects.get(id=id)
                    if feedback.answer and not request.user.is_superuser:
                        feedback.answer_readed = True
                        feedback.save()
                    return redirect('/turv/feedbacks/')
                else:
                    return render(request, 'TURV/feedback-form.html', context={'form':form})



def employers_list(request):
    if request.user.is_authenticated:
        Rights = get_rights(request)
    else:
        return redirect('/accounts/login')
    
    user_ = request.user
    

    if not Rights['granted'] or Rights['payment_department']:
        deps = Department.objects.all().filter(user=user_.id)
        employers = Employers.objects.filter(fired=0).filter(department_id__in=deps.values_list('id'))
        pag = 20
    if Rights['granted'] or Rights['payment_department']:
        deps = Department.objects.filter(notused=0).filter(is_aup=0)
        employers = Employers.objects.filter(fired=0)
        pag = 20

    if request.GET.get('search-sign', ''):

        if not Rights['granted']:
            department_permission = list(Department.objects.all().filter(user=user_.id).values_list('id'))
        if Rights['granted'] or Rights['payment_department']:
            department_permission = 'all'


        search_query = {
        'in_fired'              :request.GET.get('employers-search-fired', ''),
        'name'                  :request.GET.get('emp',                    ''),
        'department'            :request.GET.get('emp_dep',                ''),
        'shift'                 :request.GET.get('emp_shift',              ''),
        'department_permission' :department_permission
        }   

        employers = search_employers(search_query)
        pag = 1000

    p_emps = Paginator(employers, pag)
    page_number = request.GET.get('page', 1)
    page = p_emps.get_page(page_number)
    count = len(employers)
    return render(request, 'TURV/employers.html', context={'employers':              page,
                                                            'count':                 count,
                                                            'deps':                  deps,
                                                            'IsPaymentDepartment':   Rights['payment_department']
                                                            })

def new_employer(request):
    if request.user.is_authenticated:
        user_ = request.user
        u_group = user_.groups.all()
        granted = False
        aup_deps = []
        for group in u_group:
            if group.name == 'Сотрудник СУП':
                granted = True
        if (request.user.is_superuser) or (granted == True):
            deps = Department.objects.all()
            aup_deps = Department.objects.all().filter(is_aup=1)

        else:
            deps = Department.objects.all().filter(user=user_.id)
        emp_form = Employer_form()
        if request.method == 'POST':
            emp_form = Employer_form(request.POST)
            if emp_form.is_valid():
                user_ = request.user.first_name
                emp_form.saveFirst()
                loc = '/turv/employers'
                return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'TURV/new_employer.html', context={'emp':emp_form, 'deps':deps, 'aup_deps':aup_deps})

def upd_employer(request, id):
    if request.user.is_authenticated:
        Rights = get_rights(request)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    
    if request.method == "GET":
        emp = Employers.objects.get(id=id)
        fio = emp.fullname
        user_ = request.user
        u_group = user_.groups.all()
        granted = False
       
        
        if Rights['granted'] or Rights['payment_department']:
            deps = Department.objects.all()
        else:
            deps = Department.objects.all().filter(user=user_.id)
        
        emp_form = Employer_form(instance=emp)
        return render(request, 'TURV/upd_employer.html', context={'emp':                    emp_form,
                                                                  'emp_':                   emp,
                                                                  'name':                   fio,
                                                                  'deps':                   deps,
                                                                  'IsPaymentDepartment':    Rights['payment_department']})
    else:
        emp = Employers.objects.get(id=id)
        emp_form = Employer_form(request.POST, instance=emp)
        if emp_form.is_valid():
            user_ = request.user.first_name
            emp_form.save()
            loc = '/turv/close'
            return redirect(loc)

        

def del_employer(request, id):
    if request.user.is_authenticated:
        emp = Employers.objects.get(id=id)
        emp.delete()
        loc = '/turv/employers'
        return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')

def positions_list(request):
    if request.user.is_authenticated:
        search_query = {}
        if request.GET.get('search-sign', '') == '1':
            search_query = {
                'name': request.GET.get('positions-search-name', '')
            }
            positions = search_position(search_query)
        else: 
            positions = Position.objects.all().order_by('name')
        
        p_pos = Paginator(positions, 20)
        page_number = request.GET.get('page', 1)
        page = p_pos.get_page(page_number)
        return render(request, 'TURV/positions.html', context={'positions':page})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def new_position(request):
    if request.user.is_authenticated:

        positions_form = Position_form()

        if request.method == "POST":
            positions_form = Position_form(request.POST)
            if positions_form.is_valid():
                positions_form.saveFirst()
                loc = '/turv/positions'
                return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'TURV/new_position.html', context={'pos':positions_form})

def upd_position(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            pos = Position.objects.get(id=id)
            positions_form = Position_form(instance=pos)
            return render(request, 'TURV/upd_position.html', context={'pos':positions_form})
        else:
                pos = Position.objects.get(id=id)
                positions_form = Position_form(request.POST, instance=pos)
                if positions_form.is_valid():
                    positions_form.save()
                    loc = '/turv/positions'
                    return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')

def autos(request):
    if request.user.is_authenticated:
        car = request.GET.get('car','')
        if car:
            automobiles = Automobile.objects.filter(number__contains=car)
        else:
            automobiles = Automobile.objects.all()
        pag = 40
        p_autos = Paginator(automobiles, pag)
        page_number = request.GET.get('page', 1)
        page = p_autos.get_page(page_number)
        count = len(automobiles)
        return render(request, 'TURV/autos.html', context={'automobiles':page, 'count':count})

def nr_autos(request):
    if request.user.is_authenticated:
        form = Automobile_form()
        if request.method == 'POST':
            form = Automobile_form(request.POST)
            if form.is_valid():
                form.saveFirst()
                return render(request, 'TURV/close.html')
        else:
            return render(request, 'TURV/new_auto.html', context={'form':form})

def edit_autos(request,id):
    if request.user.is_authenticated:
        car = Automobile.objects.get(id=id)
        if request.method == 'GET':
            form = Automobile_form(instance=car)
            return render(request, 'TURV/new_auto.html', context={'form':form})
        else:
            form = Automobile_form(request.POST, instance=car)
            if form.is_valid():
                form.save()
                return redirect('/turv/autos')

def total_tabels(request, month, year, dep):
    # if request.user.is_authenticated:
    dict = {}
    types = TabelType.objects.all()
    deps = Department.objects.all().filter(notused=0).order_by('name')
    tabels = Tabel.objects.filter(month=month).filter(year=year).filter(department_id=dep).filter(day='0').filter(del_check=0).filter(iscorr=0).values('department__name','department_id','type_id', 'sup_check', 'paper_check')
    print(tabels)
    tabels = list(tabels)
    return JsonResponse(tabels, safe=False)

def total_tabels_html(request):
    if request.user.is_authenticated:
        deps = Department.objects.all().filter(notused=0)

        return render(request, 'TURV/total.html', context={'deps':deps})


# =========== Выгрузка ======

def old_unload(request):
    udeps = request.GET.get('udeps','')
    notulonl =  request.GET.get('nounload_only','')
    month_ = request.GET.get('uload_month','')
    if udeps:
        udeps_l = []
        udeps = udeps.split(',')
        for dep in udeps:
            udeps_l.append(dep)
        deps = Department.objects.filter(id__in=udeps_l)
    else:
        deps = Department.objects.all().order_by('id')
    year_ = request.GET.get('uload_year','')
    if month_ and year_:

        wb = xlwt.Workbook()

        for dep in deps:
            dn = str(dep.name).replace(' ','_')
            dn = dn.replace('-','')
            dn = dn.replace('(','')
            dn = dn.replace(')','')
            dn = transliterate(dn)

            if notulonl == "1":
                items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month_).filter(year=year_).filter(bound_tabel__unloaded=False).filter(bound_tabel__type__id = 1).order_by('employer')
            else:
                items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month_).filter(year=year_).filter(bound_tabel__type__id = 1).order_by('employer')






            if items:
                ct = items[0].bound_tabel.id
                current_tabel = Tabel.objects.get(id=ct)
                if items and current_tabel.sup_check == True:
                    ws = wb.add_sheet(dn)



                    i = 1
                    ws.write(0,0,'fio_vod')
                    ws.write(0,1,'dolgn')
                    ws.write(0,2,'t1')
                    ws.write(0,3,'t2')
                    ws.write(0,4,'t3')
                    ws.write(0,5,'t4')
                    ws.write(0,6,'t5')
                    ws.write(0,7,'t6')
                    ws.write(0,8,'t7')
                    ws.write(0,9,'t8')
                    ws.write(0,10,'t9')
                    ws.write(0,11,'t10')
                    ws.write(0,12,'t11')
                    ws.write(0,13,'t12')
                    ws.write(0,14,'t13')
                    ws.write(0,15,'t14')
                    ws.write(0,16,'t15')
                    ws.write(0,17,'t16')
                    ws.write(0,18,'t17')
                    ws.write(0,19,'t18')
                    ws.write(0,20,'t19')
                    ws.write(0,21,'t20')
                    ws.write(0,22,'t21')
                    ws.write(0,23,'t22')
                    ws.write(0,24,'t23')
                    ws.write(0,25,'t24')
                    ws.write(0,26,'t25')
                    ws.write(0,27,'t26')
                    ws.write(0,28,'t27')
                    ws.write(0,29,'t28')
                    ws.write(0,30,'t29')
                    ws.write(0,31,'t30')
                    ws.write(0,32,'t31')
                    ws.write(0,33,'pr1')
                    ws.write(0,34,'pr2')
                    ws.write(0,35,'pr3')
                    ws.write(0,36,'pr4')
                    ws.write(0,37,'pr5')
                    ws.write(0,38,'pr6')
                    ws.write(0,39,'pr7')
                    ws.write(0,40,'pr8')
                    ws.write(0,41,'pr9')
                    ws.write(0,42,'pr10')
                    ws.write(0,43,'pr11')
                    ws.write(0,44,'pr12')
                    ws.write(0,45,'pr13')
                    ws.write(0,46,'pr14')
                    ws.write(0,47,'pr15')
                    ws.write(0,48,'pr16')
                    ws.write(0,49,'pr17')
                    ws.write(0,50,'pr18')
                    ws.write(0,51,'pr19')
                    ws.write(0,52,'pr20')
                    ws.write(0,53,'pr21')
                    ws.write(0,54,'pr22')
                    ws.write(0,55,'pr23')
                    ws.write(0,56,'pr24')
                    ws.write(0,57,'pr25')
                    ws.write(0,58,'pr26')
                    ws.write(0,59,'pr27')
                    ws.write(0,60,'pr28')
                    ws.write(0,61,'pr29')
                    ws.write(0,62,'pr30')
                    ws.write(0,63,'pr31')
                    current_tabel.unloaded = True





                    for item in items:

                        if current_tabel.del_check == False:
                            ws.write(i,0, item.employer.fullname)
                            ws.write(i,1, item.employer.position.name)

                            if item.type_time1 == 'В':
                                ws.write(i,2,'В')
                            else:
                                ws.write(i,2,item.hours1)

                            if item.type_time2 == 'В':
                                ws.write(i,3,'В')
                            else:
                                ws.write(i,3,item.hours2)

                            if item.type_time3 == 'В':
                                ws.write(i,4,'В')
                            else:
                                ws.write(i,4,item.hours3)

                            if item.type_time4 == 'В':
                                ws.write(i,5,'В')
                            else:
                                ws.write(i,5,item.hours4)

                            if item.type_time5 == 'В':
                                ws.write(i,6,'В')
                            else:
                                ws.write(i,6,item.hours5)

                            if item.type_time6 == 'В':
                                ws.write(i,7,'В')
                            else:
                                ws.write(i,7,item.hours6)

                            if item.type_time7 == 'В':
                                ws.write(i,8,'В')
                            else:
                                ws.write(i,8,item.hours7)

                            if item.type_time8 == 'В':
                                ws.write(i,9,'В')
                            else:
                                ws.write(i,9,item.hours8)

                            if item.type_time9 == 'В':
                                ws.write(i,10,'В')
                            else:
                                ws.write(i,10,item.hours9)

                            if item.type_time10 == 'В':
                                ws.write(i,11,'В')
                            else:
                                ws.write(i,11,item.hours10)

                            if item.type_time11 == 'В':
                                ws.write(i,12,'В')
                            else:
                                ws.write(i,12,item.hours11)

                            if item.type_time12 == 'В':
                                ws.write(i,13,'В')
                            else:
                                ws.write(i,13,item.hours12)

                            if item.type_time13 == 'В':
                                ws.write(i,14,'В')
                            else:
                                ws.write(i,14,item.hours13)

                            if item.type_time14 == 'В':
                                ws.write(i,15,'В')
                            else:
                                ws.write(i,15,item.hours14)

                            if item.type_time15 == 'В':
                                ws.write(i,16,'В')
                            else:
                                ws.write(i,16,item.hours15)

                            if item.type_time16 == 'В':
                                ws.write(i,17,'В')
                            else:
                                ws.write(i,17,item.hours16)

                            if item.type_time17 == 'В':
                                ws.write(i,18,'В')
                            else:
                                ws.write(i,18,item.hours17)

                            if item.type_time18 == 'В':
                                ws.write(i,19,'В')
                            else:
                                ws.write(i,19,item.hours18)

                            if item.type_time19 == 'В':
                                ws.write(i,20,'В')
                            else:
                                ws.write(i,20,item.hours19)

                            if item.type_time20 == 'В':
                                ws.write(i,21,'В')
                            else:
                                ws.write(i,21,item.hours20)

                            if item.type_time21 == 'В':
                                ws.write(i,22,'В')
                            else:
                                ws.write(i,22,item.hours21)

                            if item.type_time22 == 'В':
                                ws.write(i,23,'В')
                            else:
                                ws.write(i,23,item.hours22)

                            if item.type_time23 == 'В':
                                ws.write(i,24,'В')
                            else:
                                ws.write(i,24,item.hours23)

                            if item.type_time24 == 'В':
                                ws.write(i,25,'В')
                            else:
                                ws.write(i,25,item.hours24)

                            if item.type_time25 == 'В':
                                ws.write(i,26,'В')
                            else:
                                ws.write(i,26,item.hours25)

                            if item.type_time26 == 'В':
                                ws.write(i,27,'В')
                            else:
                                ws.write(i,27,item.hours26)

                            if item.type_time27 == 'В':
                                ws.write(i,28,'В')
                            else:
                                ws.write(i,28,item.hours27)

                            if item.type_time28 == 'В':
                                ws.write(i,29,'В')
                            else:
                                ws.write(i,29,item.hours28)

                            if item.type_time29 == 'В':
                                ws.write(i,30,'В')
                            else:
                                ws.write(i,30,item.hours29)

                            if item.type_time30 == 'В':
                                ws.write(i,31,'В')
                            else:
                                ws.write(i,31,item.hours30)

                            if item.type_time31 == 'В':
                                ws.write(i,32,'В')
                            else:
                                ws.write(i,32,item.hours31)
                            ws.write(i,33,item.type_time1)
                            ws.write(i,34,item.type_time2)
                            ws.write(i,35,item.type_time3)
                            ws.write(i,36,item.type_time4)
                            ws.write(i,37,item.type_time5)
                            ws.write(i,38,item.type_time6)
                            ws.write(i,39,item.type_time7)
                            ws.write(i,40,item.type_time8)
                            ws.write(i,41,item.type_time9)
                            ws.write(i,42,item.type_time10)
                            ws.write(i,43,item.type_time11)
                            ws.write(i,44,item.type_time12)
                            ws.write(i,45,item.type_time13)
                            ws.write(i,46,item.type_time14)
                            ws.write(i,47,item.type_time15)
                            ws.write(i,48,item.type_time16)
                            ws.write(i,49,item.type_time17)
                            ws.write(i,50,item.type_time18)
                            ws.write(i,51,item.type_time19)
                            ws.write(i,52,item.type_time20)
                            ws.write(i,53,item.type_time21)
                            ws.write(i,54,item.type_time22)
                            ws.write(i,55,item.type_time23)
                            ws.write(i,56,item.type_time24)
                            ws.write(i,57,item.type_time25)
                            ws.write(i,58,item.type_time26)
                            ws.write(i,59,item.type_time27)
                            ws.write(i,60,item.type_time28)
                            ws.write(i,61,item.type_time29)
                            ws.write(i,62,item.type_time30)
                            ws.write(i,63,item.type_time31)
                            i = i+1
                    current_tabel.save()
        name = str(month_)+'_'+str(year_)+'.xls'
        wb.save(name)

        fp = open(name, "rb")
        response = HttpResponse(fp.read())
        fp.close();

        file_type = 'application/octet-stream'
        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(name).st_size)
        response['Content-Disposition'] = "attachment; filename=%s" %name

        return response;




    else:
        return render(request, 'TURV/unload.html', context={"deps":deps})

# ===========================

# Выгрузка основных с учетом корректировок

def unload(request):
    udeps = request.GET.get('udeps','')
    notulonl =  request.GET.get('nounload_only','')
    month_ = request.GET.get('uload_month','')
    year_ = request.GET.get('uload_year','')
    if udeps:
        udeps_l = []
        udeps = udeps.split(',')
        for dep in udeps:
            udeps_l.append(dep)
        deps = Department.objects.filter(id__in=udeps_l).order_by('id')
    else:
        deps = Department.objects.all().order_by('id')

    if month_ and year_:
        print(notulonl)
        if notulonl == '1':
            tabels = Tabel.objects.filter(department__in=deps).filter(year=year_).filter(month=month_).filter(type_id=1).filter(iscorr=0).filter(sup_check=1).filter(unloaded=0)
        else:
            tabels = Tabel.objects.filter(department__in=deps).filter(year=year_).filter(month=month_).filter(type_id=1).filter(iscorr=0).filter(sup_check=1)
    else:
        tabels = []

    if tabels:
        print(tabels)
        wb = xlwt.Workbook()
        for tabel in tabels:
            if tabel.sup_check:
                c_tabels = Tabel.objects.filter(iscorr=1).filter(corr_id=tabel.id).filter(sup_check=1).order_by('-id').filter(type_id=1)
                if c_tabels:
                    # Если корректировка одна
                    if len(c_tabels) == 1:
                        corr_emps = []
                        corr_items = []
                        c_items = TabelItem.objects.filter(bound_tabel_id=c_tabels[0])
                        for item in c_items:
                            corr_emps.append(item.employer_id)
                        items = TabelItem.objects.filter(~Q(employer_id__in=corr_emps)).filter(bound_tabel=tabel)
                        for i in items:
                            corr_items.append(i.id)
                        for i in c_items:
                            corr_items.append(i.id)
                        items = TabelItem.objects.filter(id__in=corr_items).order_by('employer')
                    # Ежели нет
                    else:
                        corr_emps = []
                        corr_items = []
                        corr_tabels = []
                        for c_tabel in c_tabels:
                            corr_tabels.append(c_tabel.id)
                        c_items = TabelItem.objects.filter(bound_tabel_id__in=corr_tabels).order_by('-bound_tabel_id')
                        for item in c_items:
                            c_emps = c_items.filter(employer_id=item.employer_id)
                            if len(c_emps) == 1:
                                corr_emps.append(item.employer_id)
                                corr_items.append(item.id)
                            else:
                                last = c_emps.latest('id')
                                corr_emps.append(last.employer_id)
                                corr_items.append(last.id)
                        items = TabelItem.objects.filter(~Q(employer_id__in=corr_emps)).filter(bound_tabel=tabel)
                        for i in items:
                            corr_items.append(i.id)
                        items = TabelItem.objects.filter(id__in=corr_items).order_by('employer')







                else:
                    items = TabelItem.objects.filter(bound_tabel=tabel).order_by('employer')
            else:
                pass

            if items:
                dn = str(tabel.department.name).replace(' ', '_')
                dn = dn.replace('-','')
                dn = dn.replace('(','')
                dn = dn.replace(')','')
                dn = transliterate(dn)

                ws = wb.add_sheet(dn)

                i = 1
                ws.write(0,0,'fio_vod')
                ws.write(0,1,'dolgn')
                ws.write(0,2,'t1')
                ws.write(0,3,'t2')
                ws.write(0,4,'t3')
                ws.write(0,5,'t4')
                ws.write(0,6,'t5')
                ws.write(0,7,'t6')
                ws.write(0,8,'t7')
                ws.write(0,9,'t8')
                ws.write(0,10,'t9')
                ws.write(0,11,'t10')
                ws.write(0,12,'t11')
                ws.write(0,13,'t12')
                ws.write(0,14,'t13')
                ws.write(0,15,'t14')
                ws.write(0,16,'t15')
                ws.write(0,17,'t16')
                ws.write(0,18,'t17')
                ws.write(0,19,'t18')
                ws.write(0,20,'t19')
                ws.write(0,21,'t20')
                ws.write(0,22,'t21')
                ws.write(0,23,'t22')
                ws.write(0,24,'t23')
                ws.write(0,25,'t24')
                ws.write(0,26,'t25')
                ws.write(0,27,'t26')
                ws.write(0,28,'t27')
                ws.write(0,29,'t28')
                ws.write(0,30,'t29')
                ws.write(0,31,'t30')
                ws.write(0,32,'t31')
                ws.write(0,33,'pr1')
                ws.write(0,34,'pr2')
                ws.write(0,35,'pr3')
                ws.write(0,36,'pr4')
                ws.write(0,37,'pr5')
                ws.write(0,38,'pr6')
                ws.write(0,39,'pr7')
                ws.write(0,40,'pr8')
                ws.write(0,41,'pr9')
                ws.write(0,42,'pr10')
                ws.write(0,43,'pr11')
                ws.write(0,44,'pr12')
                ws.write(0,45,'pr13')
                ws.write(0,46,'pr14')
                ws.write(0,47,'pr15')
                ws.write(0,48,'pr16')
                ws.write(0,49,'pr17')
                ws.write(0,50,'pr18')
                ws.write(0,51,'pr19')
                ws.write(0,52,'pr20')
                ws.write(0,53,'pr21')
                ws.write(0,54,'pr22')
                ws.write(0,55,'pr23')
                ws.write(0,56,'pr24')
                ws.write(0,57,'pr25')
                ws.write(0,58,'pr26')
                ws.write(0,59,'pr27')
                ws.write(0,60,'pr28')
                ws.write(0,61,'pr29')
                ws.write(0,62,'pr30')
                ws.write(0,63,'pr31')

                for item in items:
                    ws.write(i,0, item.employer.fullname)
                    ws.write(i,1, item.employer.position.name)

                    if item.type_time1 == 'В':
                        ws.write(i,2,'В')
                    else:
                        ws.write(i,2,item.hours1)

                    if item.type_time2 == 'В':
                        ws.write(i,3,'В')
                    else:
                        ws.write(i,3,item.hours2)

                    if item.type_time3 == 'В':
                        ws.write(i,4,'В')
                    else:
                        ws.write(i,4,item.hours3)

                    if item.type_time4 == 'В':
                        ws.write(i,5,'В')
                    else:
                        ws.write(i,5,item.hours4)

                    if item.type_time5 == 'В':
                        ws.write(i,6,'В')
                    else:
                        ws.write(i,6,item.hours5)

                    if item.type_time6 == 'В':
                        ws.write(i,7,'В')
                    else:
                        ws.write(i,7,item.hours6)

                    if item.type_time7 == 'В':
                        ws.write(i,8,'В')
                    else:
                        ws.write(i,8,item.hours7)

                    if item.type_time8 == 'В':
                        ws.write(i,9,'В')
                    else:
                        ws.write(i,9,item.hours8)

                    if item.type_time9 == 'В':
                        ws.write(i,10,'В')
                    else:
                        ws.write(i,10,item.hours9)

                    if item.type_time10 == 'В':
                        ws.write(i,11,'В')
                    else:
                        ws.write(i,11,item.hours10)

                    if item.type_time11 == 'В':
                        ws.write(i,12,'В')
                    else:
                        ws.write(i,12,item.hours11)

                    if item.type_time12 == 'В':
                        ws.write(i,13,'В')
                    else:
                        ws.write(i,13,item.hours12)

                    if item.type_time13 == 'В':
                        ws.write(i,14,'В')
                    else:
                        ws.write(i,14,item.hours13)

                    if item.type_time14 == 'В':
                        ws.write(i,15,'В')
                    else:
                        ws.write(i,15,item.hours14)

                    if item.type_time15 == 'В':
                        ws.write(i,16,'В')
                    else:
                        ws.write(i,16,item.hours15)

                    if item.type_time16 == 'В':
                        ws.write(i,17,'В')
                    else:
                        ws.write(i,17,item.hours16)

                    if item.type_time17 == 'В':
                        ws.write(i,18,'В')
                    else:
                        ws.write(i,18,item.hours17)

                    if item.type_time18 == 'В':
                        ws.write(i,19,'В')
                    else:
                        ws.write(i,19,item.hours18)

                    if item.type_time19 == 'В':
                        ws.write(i,20,'В')
                    else:
                        ws.write(i,20,item.hours19)

                    if item.type_time20 == 'В':
                        ws.write(i,21,'В')
                    else:
                        ws.write(i,21,item.hours20)

                    if item.type_time21 == 'В':
                        ws.write(i,22,'В')
                    else:
                        ws.write(i,22,item.hours21)

                    if item.type_time22 == 'В':
                        ws.write(i,23,'В')
                    else:
                        ws.write(i,23,item.hours22)

                    if item.type_time23 == 'В':
                        ws.write(i,24,'В')
                    else:
                        ws.write(i,24,item.hours23)

                    if item.type_time24 == 'В':
                        ws.write(i,25,'В')
                    else:
                        ws.write(i,25,item.hours24)

                    if item.type_time25 == 'В':
                        ws.write(i,26,'В')
                    else:
                        ws.write(i,26,item.hours25)

                    if item.type_time26 == 'В':
                        ws.write(i,27,'В')
                    else:
                        ws.write(i,27,item.hours26)

                    if item.type_time27 == 'В':
                        ws.write(i,28,'В')
                    else:
                        ws.write(i,28,item.hours27)

                    if item.type_time28 == 'В':
                        ws.write(i,29,'В')
                    else:
                        ws.write(i,29,item.hours28)

                    if item.type_time29 == 'В':
                        ws.write(i,30,'В')
                    else:
                        ws.write(i,30,item.hours29)

                    if item.type_time30 == 'В':
                        ws.write(i,31,'В')
                    else:
                        ws.write(i,31,item.hours30)

                    if item.type_time31 == 'В':
                        ws.write(i,32,'В')
                    else:
                        ws.write(i,32,item.hours31)
                    ws.write(i,33,item.type_time1)
                    ws.write(i,34,item.type_time2)
                    ws.write(i,35,item.type_time3)
                    ws.write(i,36,item.type_time4)
                    ws.write(i,37,item.type_time5)
                    ws.write(i,38,item.type_time6)
                    ws.write(i,39,item.type_time7)
                    ws.write(i,40,item.type_time8)
                    ws.write(i,41,item.type_time9)
                    ws.write(i,42,item.type_time10)
                    ws.write(i,43,item.type_time11)
                    ws.write(i,44,item.type_time12)
                    ws.write(i,45,item.type_time13)
                    ws.write(i,46,item.type_time14)
                    ws.write(i,47,item.type_time15)
                    ws.write(i,48,item.type_time16)
                    ws.write(i,49,item.type_time17)
                    ws.write(i,50,item.type_time18)
                    ws.write(i,51,item.type_time19)
                    ws.write(i,52,item.type_time20)
                    ws.write(i,53,item.type_time21)
                    ws.write(i,54,item.type_time22)
                    ws.write(i,55,item.type_time23)
                    ws.write(i,56,item.type_time24)
                    ws.write(i,57,item.type_time25)
                    ws.write(i,58,item.type_time26)
                    ws.write(i,59,item.type_time27)
                    ws.write(i,60,item.type_time28)
                    ws.write(i,61,item.type_time29)
                    ws.write(i,62,item.type_time30)
                    ws.write(i,63,item.type_time31)
                    i = i+1
                    tabel = Tabel.objects.get(id=item.bound_tabel_id)
                    tabel.unloaded = True
                    tabel.save()

            else:
                pass
        name = str(month_)+'_'+str(year_)+'.xls'
        wb.save(name)

        fp = open(name, "rb")
        response = HttpResponse(fp.read())
        fp.close();

        file_type = 'application/octet-stream'
        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(name).st_size)
        response['Content-Disposition'] = "attachment; filename=%s" %name

        return response;

    else:
        message = 'Табелей для выгрузки нет!'
        return render(request, 'TURV/unload.html', context={"deps":deps, 'message':message})

# ==========================

# Выгрузка вредности

def toxic_unload(request):
    if request.user.is_authenticated:
        month = request.GET.get('month', '')
        notulonl =  request.GET.get('nounload_only','')
        year = request.GET.get('year', '')
        deps = Department.objects.all()
        sep = '\\'

        if month and year:


            for dep in deps:
                dn = str(dep.name).replace(' ','_')
                dn = dn.replace('-','')
                dn = dn.replace('(','')
                dn = dn.replace(')','')
                dn = transliterate(dn)

                if notulonl == "1":
                    items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month).filter(year=year).filter(bound_tabel__unloaded=0).filter(bound_tabel__type_id = 2).filter(bound_tabel__sup_check=1).order_by('employer')
                    print(items)
                else:
                    items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month).filter(bound_tabel__type_id = 2).filter(year=year).filter(bound_tabel__sup_check=1).order_by('employer')
                    print(items)

                if items:
                    print(items)

                    ct = items[0].bound_tabel.id
                    current_tabel = Tabel.objects.get(id=ct)
                    if current_tabel.sup_check == True:
                        wb = xlwt.Workbook()
                        ws = wb.add_sheet("Лист1")

                        i = 0
                        for item in items:
                            # 1111
                            if item.w_hours != 0:
                                ws.write(i,0,item.employer.fullname)
                                ws.write(i,1,item.toxic_p)
                                ws.write(i,2,item.w_hours)
                                i = i+1
                        current_tabel.unloaded = True
                        current_tabel.save()
                        # name =  'S:\Сетевые папки\Обмен\Бухгалтерия\РАСЧЕТНЫЙ ОТДЕЛ\ВыгрузкаВредности' + sep + str(dn) + '_' + str(month)+'_'+str(year)+ '_vrednost.xls'
                        name =  '/mnt/1c-u-HRD_Uploads/ВыгрузкаВредности/' + str(dn) + '_' + str(month)+'_'+str(year)+ '_vrednost.xls'

                        wb.save(name)



                else:
                    pass







            # fp = open(name, "rb")
            # response = HttpResponse(fp.read())
            # fp.close();
            #
            # file_type = 'application/octet-stream'
            # response['Content-Type'] = file_type
            # response['Content-Length'] = str(os.stat(name).st_size)
            # response['Content-Disposition'] = "attachment; filename=%s" %name

            return render(request, 'TURV/toxic-unload.html')
        else:
            return render(request, 'TURV/toxic-unload.html')

# ===========================

# Выгрузка совмещения

def unite_unload(request):
    if request.user.is_authenticated:
        month = request.GET.get('month', '')
        notulonl =  request.GET.get('nounload_only','')
        year = request.GET.get('year', '')
        deps = Department.objects.all()
        sep = '\\'

        if month and year:


            for dep in deps:
                dn = str(dep.name).replace(' ','_')
                dn = dn.replace('-','')
                dn = dn.replace('(','')
                dn = dn.replace(')','')
                dn = transliterate(dn)

                if notulonl == "1":
                    items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month).filter(year=year).filter(bound_tabel__unloaded=False).filter(bound_tabel__type_id = 3).order_by('employer')

                else:
                    items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month).filter(bound_tabel__type_id = 3).filter(year=year).order_by('employer')


                if items:

                    ct = items[0].bound_tabel.id
                    current_tabel = Tabel.objects.get(id=ct)
                    if current_tabel.sup_check == True:
                        wb = xlwt.Workbook()
                        ws = wb.add_sheet("Лист1")

                        i = 0
                        for item in items:
                            print(item)
                            if item.w_hours != 0:
                                ws.write(i,0,item.employer.fullname)
                                ws.write(i,1,item.auto.unite_p)
                                ws.write(i,2,item.employer.stand_worktime)
                                ws.write(i,3,item.w_hours)
                                ws.write(i,4,item.employer.positionOfPayment)
                                i = i+1
                        current_tabel.unloaded = True
                        current_tabel.save()
                        '/samba/users/toxic/'
                        # name =  'S:\Сетевые папки\Обмен\Бухгалтерия\РАСЧЕТНЫЙ ОТДЕЛ\ВыгрузкаСовмещения' + sep + str(dn) + '_' + str(month)+'_'+str(year)+ '_sovmesheniye.xls'
                        name =  '/mnt/1c-u-HRD_Uploads/ВыгрузкаСовмещения/' + str(dn) + '_' + str(month)+'_'+str(year)+ '_sovmesheniye.xls'
                        print(name)
                        wb.save(name)


                else:
                    pass




            return render(request, 'TURV/unite-unload.html')
        else:
            return render(request, 'TURV/unite-unload.html')

# =========================

# Выгрузка молока

def milk_unload(request):
    if request.user.is_authenticated:
        month = request.GET.get('month', '')
        notulonl =  request.GET.get('nounload_only','')
        year = request.GET.get('year', '')
        deps = Department.objects.all()
        sep = '\\'

        if month and year:


            for dep in deps:
                dn = str(dep.name).replace(' ','_')
                dn = dn.replace('-','')
                dn = dn.replace('(','')
                dn = dn.replace(')','')
                dn = transliterate(dn)

                if notulonl == "1":
                    items = TabelItem.objects.filter(employer__department_id=dep.id).filter(bound_tabel__month=month).filter(bound_tabel__year=year).filter(bound_tabel__unloaded=False).filter(bound_tabel__type_id = 9).order_by('employer')

                else:
                    items = TabelItem.objects.filter(employer__department_id=dep.id).filter(bound_tabel__month=month).filter(bound_tabel__type_id = 9).filter(bound_tabel__year=year).order_by('employer')


                if items:

                    ct = items[0].bound_tabel.id
                    current_tabel = Tabel.objects.get(id=ct)
                    if current_tabel.del_check == False:
                        wb = xlwt.Workbook()
                        ws = wb.add_sheet("Лист1")

                        i = 0
                        for item in items:
                            print(item)
                            if item.w_hours != 0:
                                ws.write(i,0,item.employer.fullname)
                                ws.write(i,1,item.w_hours)
                                i = i+1
                        current_tabel.unloaded = True
                        current_tabel.save()
                        '/samba/users/toxic/'
                        # name =  'S:\Сетевые папки\Обмен\Бухгалтерия\РАСЧЕТНЫЙ ОТДЕЛ\ВыгрузкаМолока' + sep + str(dn) + '_' + str(month)+'_'+str(year)+ '_milk.xls'
                        name =  '/mnt/1c-u-HRD_Uploads/ВыгрузкаМолока/' + str(dn) + '_' + str(month)+'_'+str(year)+ '_milk.xls'
                        print(name)
                        wb.save(name)


                else:
                    pass




            return render(request, 'TURV/milk-unload.html')
        else:
            return render(request, 'TURV/milk-unload.html')

# =========================

# ---------------------------

# ===== Работа с нормой =======

def upd_norma(request):
    if request.user.is_authenticated:
        norms = Overtime.objects.all()

        return render(request, 'TURV/overtime.html', context={'norms':norms})

@login_required
def add_norma(request):
    if request.method == "GET":
        form = OvertimeUpdate_form()
        return render(request, 'TURV/new_overtime.html', context={'form':form})
    if request.method == "POST":
        form = OvertimeUpdate_form(request.POST)
        if form.is_valid():
            form.saveFirst()
            return redirect('/turv/overtime/')
        else:
            return render(request, 'TURV/new_overtime.html', context={'form':form, 'errors':form.errors.as_text()})


def new_norma(request):
    if request.user.is_authenticated:
        current_date = str(DT.datetime.today().year)
        current_date = current_date + "-01-01"
        current_norma = Overtime.objects.filter(year=current_date)
        current_norma_m = current_norma[0].value_m
        current_norma_w = current_norma[0].value_w

        emps_m = Employers.objects.filter(sex='М').filter(shift_personnel=1)
        for m in emps_m:
            m.stand_worktime = current_norma_m
            m.save()

        emps_w = Employers.objects.filter(sex='Ж').filter(shift_personnel=1)
        for w in emps_w:
            w.stand_worktime = current_norma_w
            w.save()
        message = "Норма обновлена!"


        return JsonResponse(message, safe=False)

# ==============================

# Архив
def get_archive(request):
    return render(request, 'TURV/archive.html', context={})