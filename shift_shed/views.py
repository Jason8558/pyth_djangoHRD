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
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph


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

@login_required
def ss_print(request, id):
    shed = ShiftShedModel.objects.get(id=id)
    employee = ResEmloyee.objects.filter(dep=shed.dep)
    cal = {'1':'Январь','2':"Февраль",'3':"Март",'4':"Апрель",'5':"Май",'6':"Июнь",'7':"Июль",'8':"Август",'9':"Сентябрь",'10':"Октябрь",'11':"Ноябрь",'12':"Декабрь"}
    filename = 'График сменности ' +  shed.dep.name
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="%s"' % filename

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer, pagesize=landscape(A4))
    elements=[]
    

    pdfmetrics.registerFont(TTFont('FreeSans', 'ZenAntiqueSoft-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('RobotoSlab', 'RobotoSlab-VariableFont_wght.ttf'))
    pdfmetrics.registerFontFamily('RobotoSlab',normal='Roboto Slab',bold='Roboto Slab ExtraBold',italic='VeraIt',boldItalic='VeraBI')
    # p.setFont('FreeSans', 14)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    style = [
       
        ('BACKGROUND',(0, 0), (36,0),colors.lightgrey),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black)]
    
    
    my_Style=ParagraphStyle('My Para style',
            fontName='FreeSans',
            # backColor='#F1F1F1',
            fontSize=9,
            # borderColor='#FFFF00',
            # borderWidth=2,
            # borderPadding=(20,20,20),
            leading=20,
            alignment=1
)
    emp_text_head = "СОГЛАСОВАНО"
    emp_text =  employee[0].pos + ' ' + employee[0].emp.fullname
    p1 = Paragraph(emp_text, my_Style)

    p.setFont('FreeSans', 10)
    p.drawString(110, 570, emp_text_head)

    p1.wrapOn(p,250,50)
    p1.drawOn(p,30,520)

    lines = "____________________________   __.___._____ г."
    p2 = Paragraph(lines, my_Style)
    p2.wrapOn(p, 300, 50)
    p2.drawOn(p, 20, 500)

    director_head = "УТВЕРЖДАЮ"
    p.drawString(650, 570, director_head)
    
    director = "Директор КГУП ""Камчатский водоканал"" Супрун А.С."
    
    p2 = Paragraph(director, my_Style)
    p2.wrapOn(p, 200, 50)
    p2.drawOn(p, 590, 520)

    p2 = Paragraph(lines, my_Style)
    p2.wrapOn(p, 300, 50)
    p2.drawOn(p, 550, 500)


    items = ShiftShedItem.objects.filter(bound_shed=shed).filter(month=1)
    data = list()
    data.append([
        'ФИО | Должн.',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
    'Факт',
    'Норма',
    'Праз.',
    'Откл.'

    ])
    for item in items:
        data.append([
        item.employer.fullname + '|' + item.employer.position.name,
        item.day_1,
        item.day_2,
        item.day_3,
        item.day_4,
        item.day_5,
        item.day_6,
        item.day_7,
        item.day_8,
        item.day_9,
        item.day_10,
        item.day_11,
        item.day_12,
        item.day_13,
        item.day_14,
        item.day_15,
        item.day_16,
        item.day_17,
        item.day_18,
        item.day_19,
        item.day_20,
        item.day_21,
        item.day_22,
        item.day_23,
        item.day_24,
        item.day_25,
        item.day_26,
        item.day_27,
        item.day_28,
        item.day_29,
        item.day_30,
        item.day_31,
        item.fact,
        item.norma,
        item.celeb,
        "%.2f" % item.deviation
        ])
    table = Table(data)
    for row, values in enumerate(data):
        for column, value in enumerate(values):
            style.append(['FONTNAME',(0,0),(column,row),'FreeSans'])
            style.append(['FONTSIZE',(column,row),(column,row),6])

    table.setStyle(TableStyle(style))

    p.setFont('RobotoSlab', 12)
    p.drawString(350, 500, "Январь")
    
    table.wrapOn(p, 100, 100)
    table.wrapOn(p, 100, 100)
    table.drawOn(p, 30, 300)

    items = ShiftShedItem.objects.filter(bound_shed=shed).filter(month=2)
    data = list()
    data.append([
        'ФИО | Должн.',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
    'Факт',
    'Норма',
    'Праз.',
    'Откл.'

    ])
    for item in items:
        data.append([
        item.employer.fullname + '|' + item.employer.position.name,
        item.day_1,
        item.day_2,
        item.day_3,
        item.day_4,
        item.day_5,
        item.day_6,
        item.day_7,
        item.day_8,
        item.day_9,
        item.day_10,
        item.day_11,
        item.day_12,
        item.day_13,
        item.day_14,
        item.day_15,
        item.day_16,
        item.day_17,
        item.day_18,
        item.day_19,
        item.day_20,
        item.day_21,
        item.day_22,
        item.day_23,
        item.day_24,
        item.day_25,
        item.day_26,
        item.day_27,
        item.day_28,
        item.day_29,
        item.day_30,
        item.day_31,
        item.fact,
        item.norma,
        item.celeb,
        "%.2f" % item.deviation
        ])
    table = Table(data)
    for row, values in enumerate(data):
        for column, value in enumerate(values):
            style.append(['FONTNAME',(0,0),(column,row),'FreeSans'])
            style.append(['FONTSIZE',(column,row),(column,row),6])

    table.setStyle(TableStyle(style))

    p.setFont('RobotoSlab', 12)
    p.drawString(350, 270, "Февраль")
    
    table.wrapOn(p, 100, 100)
    table.wrapOn(p, 100, 100)
    table.drawOn(p, 30, 50)
    
    p.showPage()
    
    months = ([3,4],[5,6],[7,8],[9,10],[11,12])
    

    
    
    for mgroup in months:
        items = ShiftShedItem.objects.filter(bound_shed=shed).filter(month=mgroup[0])
        data = list()
        data.append([
            'ФИО | Должн.',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '30',
        '31',
        'Факт',
        'Норма',
        'Праз.',
        'Откл.'

        ])
        for item in items:
            data.append([
            item.employer.fullname + '|' + item.employer.position.name,
            item.day_1,
            item.day_2,
            item.day_3,
            item.day_4,
            item.day_5,
            item.day_6,
            item.day_7,
            item.day_8,
            item.day_9,
            item.day_10,
            item.day_11,
            item.day_12,
            item.day_13,
            item.day_14,
            item.day_15,
            item.day_16,
            item.day_17,
            item.day_18,
            item.day_19,
            item.day_20,
            item.day_21,
            item.day_22,
            item.day_23,
            item.day_24,
            item.day_25,
            item.day_26,
            item.day_27,
            item.day_28,
            item.day_29,
            item.day_30,
            item.day_31,
            item.fact,
            item.norma,
            item.celeb,
            "%.2f" % item.deviation
            ])
        table = Table(data)
        for row, values in enumerate(data):
            for column, value in enumerate(values):
                style.append(['FONTNAME',(0,0),(column,row),'FreeSans'])
                style.append(['FONTSIZE',(column,row),(column,row),6])

        table.setStyle(TableStyle(style))

        p.setFont('RobotoSlab', 12)
        p.drawString(350, 560, cal[str(mgroup[0])])

        table.wrapOn(p, 100, 100)
        table.wrapOn(p, 100, 100)
        table.drawOn(p, 30, 350)
        
        items = ShiftShedItem.objects.filter(bound_shed=shed).filter(month=mgroup[1])
        data = list()

        data.append([
            'ФИО | Должн.',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '30',
        '31',
        'Факт',
        'Норма',
        'Праз.',
        'Откл.'

        ])
        for item in items:
            data.append([
            item.employer.fullname + '|' + item.employer.position.name,
            item.day_1,
            item.day_2,
            item.day_3,
            item.day_4,
            item.day_5,
            item.day_6,
            item.day_7,
            item.day_8,
            item.day_9,
            item.day_10,
            item.day_11,
            item.day_12,
            item.day_13,
            item.day_14,
            item.day_15,
            item.day_16,
            item.day_17,
            item.day_18,
            item.day_19,
            item.day_20,
            item.day_21,
            item.day_22,
            item.day_23,
            item.day_24,
            item.day_25,
            item.day_26,
            item.day_27,
            item.day_28,
            item.day_29,
            item.day_30,
            item.day_31,
            item.fact,
            item.norma,
            item.celeb,
            "%.2f" % item.deviation
            ])
        table = Table(data)
        for row, values in enumerate(data):
            for column, value in enumerate(values):
                style.append(['FONTNAME',(column,row),(column,row),'FreeSans'])
                style.append(['FONTSIZE',(column,row),(column,row),6])

        table.setStyle(TableStyle(style))

        p.setFont('RobotoSlab', 12)
        p.drawString(350, 320, cal[str(mgroup[1])])

        table.wrapOn(p, 100, 100)
        table.wrapOn(p, 100, 100)
        table.drawOn(p, 30, 100)

        p.showPage()
    
    total = additional_formtotal(id)

    total_table = list()

    total_table.append([
        'ФИО | Должн.',
        'Факт',
        'Праздничные',
        'Норма',
        'Отклонения',
        '  Ознакомлен  ',
    ])

    for rec in total:
        total_table.append([rec['emp'].fullname, rec['s_fact'], rec['s_celeb'], rec['s_norma'], "%.2f" % rec['s_dev']])
    
    table = Table(total_table)

    for row, values in enumerate(data):
        for column, value in enumerate(values):
            style.append(['FONTNAME',(column,row),(column,row),'FreeSans'])
            style.append(['FONTSIZE',(column,row),(column,row),6])

    table.setStyle(TableStyle(style))

    p.setFont('RobotoSlab', 12)
    p.drawString(370, 570, 'ИТОГИ')

    table.wrapOn(p, 100, 100)
    table.wrapOn(p, 100, 100)
    table.drawOn(p, 270, 370)

    p.drawString(100, 300, "СОГЛАСОВАНО:" )
    
    p.setFont('RobotoSlab', 10)

    p.drawString(100, 280, 'Руководитель структурного подразделения _______________________________________________________________')
    p.drawString(100, 250, 'Руководитель СУП _______________________________________________________________')
    p.drawString(100, 220, 'Председатель профкома _______________________________________________________________')
    p.showPage()



    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

