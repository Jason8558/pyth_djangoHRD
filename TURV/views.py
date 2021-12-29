from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, F, Case, When
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
import xlwt
from mimetypes import MimeTypes
import os
import datetime
from itertools import groupby
from django.contrib.auth.models import *

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

def tabels(request):
 #Проверка на аутентификацию
    if request.user.is_authenticated:
        # Переменные
        group = Group.objects.get(name__icontains='Табельщик')
        tab_users = group.user_set.all().order_by('first_name')
        sq_period_month = request.GET.get('search_month', '')
        sq_period_year = request.GET.get('search_year', '')
        sq_dep = request.GET.get('t_tab_dep_search', '')
        sq_check = request.GET.get('tab_supcheck','')
        sq_user = request.GET.get('tab_user','')
        sq_this_month = request.GET.get('this_month','')
        sq_check_this_month = request.GET.get('chk_this_month','')
        user_ = request.user
        u_group = user_.groups.all()
        is_ro = 0
        granted = 0

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

        if (granted == False):
            # если пользователь только с правами на определенные подразделения, собираем их тут:
            deps = Department.objects.all().filter(user=user_.id)
            allow_departments = []
            for dep in deps:
                allow_departments.append(dep.id)


            # Алгоритм поиска
            pag = 1000
            if (sq_period_month) and (sq_period_year):
                tabels = Tabel.objects.all().filter(department_id__in=allow_departments).filter(year=sq_period_year).filter(month=sq_period_month)
            else:
                if (sq_period_month):
                    tabels = Tabel.objects.all().filter(department_id__in=allow_departments).filter(month=sq_period_month)
                else:
                    if (sq_period_year):
                        tabels = Tabel.objects.all().filter(department_id__in=allow_departments).filter(year=sq_period_year)
                    else:
                        if (sq_this_month):
                            tabels = Tabel.objects.all().filter(department_id__in=allow_departments).filter(year=year_).filter(month=month_)
                        else:
                            pag = 40
                            tabels = Tabel.objects.all().filter(department_id__in=allow_departments).order_by('-month')


        else:
            # если у пользователя полные права, то выдаем все
            deps = Department.objects.all().order_by('name')
            # Алгоритм поиска
            pag = 1000
            if (sq_period_month) and (sq_period_year) and (sq_dep):

                tabels = Tabel.objects.all().filter(year=sq_period_year).filter(month=sq_period_month).filter(department_id=sq_dep)
            else:
                if (sq_period_year) and (sq_dep):
                    tabels = Tabel.objects.all().filter(year=sq_period_year).filter(department_id=sq_dep)
                else:
                    if (sq_period_month):
                        tabels = Tabel.objects.all().filter(month=sq_period_month)
                    else:
                        if (sq_period_year):
                            tabels = Tabel.objects.all().filter(year=sq_period_year)
                        else:
                            if (sq_dep):
                                tabels = Tabel.objects.all().filter(department_id=sq_dep).order_by('-year', '-month')
                            else:
                                if (sq_this_month):
                                    tabels = Tabel.objects.all().filter(year=year_).filter(month=month_).order_by('department__name')
                                else:
                                    if (sq_check_this_month):
                                        tabels = Tabel.objects.all().filter(year=year_).filter(month=month_).filter(sup_check= True)
                                    else:
                                        if (sq_user):
                                            tabels = Tabel.objects.all().filter(res_officer=sq_user).order_by('-year', '-month')
                                        else:
                                            pag = 40
                                            tabels = Tabel.objects.all().order_by('-year', '-month')



        p_tabels = Paginator(tabels, pag)
        page_number = request.GET.get('page', 1)
        page = p_tabels.get_page(page_number)
        count = len(tabels)



        return render(request, 'TURV/tabels.html', context={'tab_users':tab_users, 'tabels':page, 'count':count, 'deps':deps, 'granted':granted, 'ro':is_ro, 'month_':month_, "year_":year_})
    else:
        return redirect('/accounts/login/')

def tabel_create(request, id):
    if request.user.is_authenticated:
        sq_employer = request.GET.get('its_employer','')
        sq_position = request.GET.get('its_position','')
        u_group = request.user.groups.all()
        granted = 0
        is_ro = 0
        allow_print = 0
        if request.user.is_superuser:
            granted = 1
        else:
            for group in u_group:
                if (group.name == 'Сотрудник СУП'):
                    granted = 1
                if (group.name == 'Сотрудник РО'):
                    is_ro = 1
                if (group.name == 'Печать табеля'):
                    allow_print = 1
        if request.method == "GET":

            b_tabel = Tabel.objects.get(id=id)
            items = TabelItem.objects.filter(bound_tabel=id).order_by('employer__position__name').values('employer__position__name')
            positions = []
            for item in list(items):
                positions.append(item['employer__position__name'])
            positions = [el for el, _ in groupby(positions)]
            tabel_form = Tabel_form(instance=b_tabel)
            if sq_employer:
                items = TabelItem.objects.filter(bound_tabel=id).filter(employer__fullname__icontains=sq_employer).order_by('employer')
            else:
                if sq_position:
                    items = TabelItem.objects.filter(bound_tabel=id).filter(employer__position__name=sq_position).order_by('employer')
                else:
                    items = TabelItem.objects.filter(bound_tabel=id).order_by('employer')
            hours = items.aggregate(sum_of_hours=Sum("w_hours"), sum_of_lhours=Sum("sHours19"), sum_of_days=Sum("w_days"),  s_over=Sum('sHours4'), s_night=Sum("sHours2"), s_vacwork=Sum("sHours3"),     s_vac=Sum("v_days"), s_weekends=Sum("sHours24")/8)
            s_hours = hours['sum_of_hours']
            s_lhours = hours['sum_of_lhours']
            s_days = hours['sum_of_days']
            s_over = hours['s_over']
            s_night = hours['s_night']
            s_vacwork = hours['s_vacwork']
            s_vac = hours['s_vac']
            s_weekends = hours['s_weekends']

            count = len(items)
            t_month = b_tabel.month
            t_year = b_tabel.year
            t_dep = b_tabel.department
            return render(request, 'TURV/create_tabel.html', context={'positions':positions,
            's_hours':s_hours,
's_lhours':s_lhours,
's_days':s_days,
's_over':s_over,
's_night':s_night,
's_vacwork':s_vacwork,
's_vac':s_vac,
's_weekends':s_weekends,

            'hours':hours,'form':tabel_form, 'items':items, 'print':allow_print, 'month':t_month, 'year':t_year, 'count':count, 'b_tabel':b_tabel, 'granted':granted, 'ro':is_ro})

        else:
            b_tabel = Tabel.objects.get(id=id)
            bound_form = Tabel_form(request.POST, instance=b_tabel)
            if bound_form.is_valid():

                bound_form.save()
                return render(request, 'TURV/close.html')

    else:
        return render(request, 'reg_jounals/no_auth.html')

def new_tabel(request):
    if request.user.is_authenticated:
        user_ = request.user
        u_group = user_.groups.all()
        granted = 0
        for group in u_group:
            if group.name == 'Сотрудник СУП':
                granted = 1
        if (request.user.is_superuser) or (granted == 1):
            deps = Department.objects.all()
        else:
            deps = Department.objects.filter(user=user_.id)
        tabel_form = Tabel_form()
        if request.method == "POST":
            tabel_form = Tabel_form(request.POST)
            if tabel_form.is_valid():
                user_ = request.user.first_name
                tabel_form.saveFirst(user_)
                return redirect('..')

        else:

            return render(request, 'TURV/new_tabel.html', context={'form':tabel_form, 'deps':deps})
    else:
        return render(request, 'reg_jounals/no_auth.html')

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
        allow_employers = Employers.objects.filter(department_id=department)
        names = []
        for emp in allow_employers:
            names.append(emp.fullname)


        tabelItem_form = TabelItem_form()
        if request.method == "POST":
            tabelItem_form = TabelItem_form(request.POST)
            if tabelItem_form.is_valid():
                user_ = request.user.first_name
                tabelItem_form.saveFirst(id)
                loc = '/turv/create/'+str(id)
                return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')
    return render(request, 'TURV/new_tabel_item.html', context={'tabel':tabelItem_form, 'in_tabel':in_tabel_items, 'b_tabel':b_tabel, 'year':year, 'month':month, 'emps':allow_employers})

def tabel_upditem(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            item = TabelItem.objects.get(id=id)

            bound_form = TabelItem_form(instance=item)
            year = item.bound_tabel.year
            month = item.bound_tabel.month
            department = item.bound_tabel.department
            return render(request, 'TURV/upd_tabel_item.html', context={'tabel':bound_form, 'item':item, 'b_tabel':item.bound_tabel.id, 'year':year, 'month':month})

        else:
            item = TabelItem.objects.get(id=id)
            tabelItem_form = TabelItem_form(request.POST, instance=item)
            if tabelItem_form.is_valid():


                tabelItem_form.save()
                loc = '/turv/create/'+str(item.bound_tabel.id)
                return redirect(loc)
            else:
                print(tabelItem_form.errors)
    else:
        return render(request, 'reg_jounals/no_auth.html')

def tabel_sup_check(request, id):
    if request.user.is_authenticated:
            tabel = Tabel.objects.get(id=id)
            log = open('log.txt', 'a')
            if tabel.sup_check == False:
                tabel.sup_check = True
                log.write(str(DT.date.today()) + " пользователь " + request.user.first_name + " проверил табель " + str(tabel.department) + ' за ' + str(tabel.year) + '.' + str(tabel.month) + '\n'  )
            else:
                tabel.sup_check = False
                log.write(str(DT.date.today()) + " пользователь " + request.user.first_name + " снял пометку о проверке табеля " + str(tabel.department) + ' за ' + str(tabel.year) + '.' + str(tabel.month) + '\n'  )
            tabel.save()
            log.close()
    return redirect('/turv/create/' + str(id))

def tabel_delitem(request, id):
    if request.user.is_authenticated:
        item = TabelItem.objects.get(id__iexact=id)
        num = item.bound_tabel.id
        dest = '/turv/create/' + str(num)
        item.delete()
        return redirect(dest)

def employers_list(request):
    if request.user.is_authenticated:
        # Проверка пользователя и прав
        user_ = request.user
        granted = access_check(request)

        # Переменные
        sq_emp = request.GET.get('emp', '')
        sq_dep = request.GET.get('emp_dep', '')
        sq_shift = request.GET.get('emp_shift', '')

        if (granted == False):
            deps = Department.objects.all().filter(user=user_.id)
            allow_departments = []
            for dep in deps:
                allow_departments.append(dep.id)
            # Алгоритм поиска
            pag = 1000
            if (sq_emp):
                employers = Employers.objects.all().filter(department_id__in=allow_departments).filter(fullname__icontains=sq_emp)
            else:
                if (sq_dep) and (sq_shift):
                    if (sq_shift == 1):
                        employers = Employers.objects.all().filter(department_id=sq_dep).filter(shift_personnel=True)
                    else:

                        employers = Employers.objects.all().filter(department_id=sq_dep).filter(shift_personnel=False)
                else:
                    if (sq_dep):
                        employers = Employers.objects.all().filter(department_id=sq_dep)
                    else:
                        if (sq_shift == '1'):
                                employers = Employers.objects.all().filter(department_id__in=allow_departments).filter(shift_personnel=True)
                        else:
                            if (sq_shift == '2'):
                                employers = Employers.objects.all().filter(department_id__in=allow_departments).filter(shift_personnel=False)
                            else:
                                pag = 50
                                employers = Employers.objects.all().filter(department_id__in=allow_departments)

        else:
            deps = Department.objects.all()
            # Алгоритм поиска
            pag = 1000
            if (sq_emp):
                employers = Employers.objects.all().filter(fullname__icontains=sq_emp)
            else:
                if (sq_dep) and (sq_shift):
                    if (sq_shift == 1):
                        employers = Employers.objects.all().filter(department_id=sq_dep).filter(shift_personnel=True)
                    else:

                        employers = Employers.objects.all().filter(department_id=sq_dep).filter(shift_personnel=False)
                else:
                    if (sq_dep):
                        employers = Employers.objects.all().filter(department_id=sq_dep)
                    else:
                        if (sq_shift == '1'):
                                employers = Employers.objects.all().filter(shift_personnel=True)
                        else:
                            if (sq_shift == '2'):
                                employers = Employers.objects.all().filter(shift_personnel=False)
                            else:
                                pag = 50
                                employers = Employers.objects.all()




        p_emps = Paginator(employers, pag)
        page_number = request.GET.get('page', 1)
        page = p_emps.get_page(page_number)
        count = len(employers)
        return render(request, 'TURV/employers.html', context={'employers':page, 'count':count, 'deps':deps})

def new_employer(request):
    if request.user.is_authenticated:
        user_ = request.user
        u_group = user_.groups.all()
        granted = False
        for group in u_group:
            if group.name == 'Сотрудник СУП':
                granted = True
        if (request.user.is_superuser) or (granted == True):
            deps = Department.objects.all()
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
    return render(request, 'TURV/new_employer.html', context={'emp':emp_form, 'deps':deps})

def upd_employer(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            emp = Employers.objects.get(id=id)
            fio = emp.fullname
            user_ = request.user
            u_group = user_.groups.all()
            granted = False
            for group in u_group:
                if group.name == 'Сотрудник СУП':
                    granted = True
            if (request.user.is_superuser) or (granted == True):
                deps = Department.objects.all()
            else:
                deps = Department.objects.all().filter(user=user_.id)
            emp_form = Employer_form(instance=emp)
            return render(request, 'TURV/upd_employer.html', context={'emp':emp_form, 'emp_':emp, 'name':fio,  'deps':deps})
        else:
            emp = Employers.objects.get(id=id)
            emp_form = Employer_form(request.POST, instance=emp)
            if emp_form.is_valid():
                user_ = request.user.first_name
                emp_form.save()
                loc = '/turv/employers'
                return redirect(loc)
    else:
        return render(request, 'reg_jounals/no_auth.html')

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
        positions = Position.objects.all().order_by('name')
        return render(request, 'TURV/positions.html', context={'positions':positions})
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

def unload(request):
    udeps = request.GET.get('udeps','')
    notulonl =  request.GET.get('nounload_only','')
    month_ = request.GET.get('uload_month','')
    print(notulonl)
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
                items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month_).filter(year=year_).filter(bound_tabel__unloaded=False).order_by('employer')
            else:
                items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month_).filter(year=year_).order_by('employer')


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

def upd_norma(request):
    if request.user.is_authenticated:
        norms = Overtime.objects.all()

        return render(request, 'TURV/overtime.html', context={'norms':norms})

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
