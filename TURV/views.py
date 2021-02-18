from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
import xlwt



def tabels(request):
    if request.user.is_authenticated:
        user_ = request.user
        u_group = user_.groups.all()

        granted = 0
        for group in u_group:
            if group.name == 'Сотрудник СУП':
                granted = 1
        if (request.user.is_superuser) or (granted == 1):
            tabels = Tabel.objects.all()
        else:

            deps = Department.objects.all().filter(user=user_.id)
            allow_departments = []
            for dep in deps:
                allow_departments.append(dep.id)

            tabels = Tabel.objects.all().filter(department_id__in=allow_departments)
        p_tabels = Paginator(tabels, 15)
        page_number = request.GET.get('page', 1)
        page = p_tabels.get_page(page_number)
        count = len(tabels)
        return render(request, 'TURV/tabels.html', context={'tabels':page, 'count':count})
    else:
        return render(request, 'reg_jounals/no_auth.html')

def tabel_create(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            b_tabel = Tabel.objects.get(id=id)
            tabel_form = Tabel_form(instance=b_tabel)
            items = TabelItem.objects.filter(bound_tabel=id).order_by('employer')
            count = len(items)
            t_month = b_tabel.month
            t_year = b_tabel.year
            t_dep = b_tabel.department
            return render(request, 'TURV/create_tabel.html', context={'form':tabel_form, 'items':items, 'month':t_month, 'year':t_year, 'count':count, 'b_tabel':b_tabel})
        else:
            b_tabel = Tabel.objects.get(id=id)
            bound_form = Tabel_form(request.POST, instance=b_tabel)
            if bound_form.is_valid():

                bound_form.save()
                return redirect('/turv/')

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
            b_tabel = Tabel.objects.get(id=item.bound_tabel)
            bound_form = TabelItem_form(instance=item)
            year = b_tabel.year
            month = b_tabel.month
            department = b_tabel.department
            return render(request, 'TURV/upd_tabel_item.html', context={'tabel':bound_form, 'item':item, 'b_tabel':b_tabel, 'year':year, 'month':month})

        else:
            item = TabelItem.objects.get(id=id)
            tabelItem_form = TabelItem_form(request.POST, instance=item)
            if tabelItem_form.is_valid():


                tabelItem_form.save()
                loc = '/turv/create/'+str(item.bound_tabel)
                return redirect(loc)
            else:
                print(tabelItem_form.errors)
    else:
        return render(request, 'reg_jounals/no_auth.html')

def tabel_delitem(request, id):
    if request.user.is_authenticated:
        item = TabelItem.objects.get(id__iexact=id)
        num = item.bound_tabel
        dest = '/turv/create/' + str(num)
        item.delete()
        return redirect(dest)

def employers_list(request):
    if request.user.is_authenticated:
        user_ = request.user
        u_group = user_.groups.all()
        granted = False
        for group in u_group:
            if group.name == 'Сотрудник СУП':
                granted = True
        if (request.user.is_superuser) or (granted == True):
            employers = Employers.objects.all()
        else:
            deps = Department.objects.all().filter(user=user_.id)
            allow_departments = []
            for dep in deps:
                allow_departments.append(dep.id)

            employers = Employers.objects.all().filter(department_id__in=allow_departments)
        count = len(employers)
        return render(request, 'TURV/employers.html', context={'employers':employers, 'count':count})

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

    month_ = request.GET.get('uload_month','')

    year_ = request.GET.get('uload_year','')
    if month_ and year_:
        wb = xlwt.Workbook()

        deps = Department.objects.all().order_by('id')

        for dep in deps:
            ws = wb.add_sheet(dep.name)
            items = TabelItem.objects.filter(employer__department_id=dep.id).filter(month=month_).filter(year=year_)


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
                current_tabel = Tabel.objects.get(id=item.bound_tabel)
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

        name = str(month_)+'_'+str(year_)+'.xls'
        wb.save(name)
        return redirect('/turv')
    else:
        return render(request, 'TURV/unload.html')





def upd_norma_test(request):
    emps = list(Employers.objects.filter(department_id=2))
    for emp in emps:

        emp.stand_worktime = 164.33
    Employers.objects.bulk_update(emps, ['stand_worktime'])
    return redirect('/turv/')