from .models import TabelItem, Position, Employers, Tabel as TabelModel
from work_cal.models import WorkCalendarRecord
import calendar
from vac_shed.views import *
from django.shortcuts import redirect
import json

def search_tabel_item(search_query: dict):
    items = TabelItem.objects.filter(bound_tabel_id=search_query['tabel_id']).filter(
        employer__fullname__icontains=search_query['name']).filter(
        employer__position__name__icontains=search_query['position']).order_by(
        'employer__fullname')
    
    return items

def search_position(search_query: dict):
    items = Position.objects.filter(name__icontains=search_query['name']).order_by('name')

    return items

def search_employers(search_query: dict):
        if search_query['department_permission'] != 'all':
           items = Employers.objects.filter(department_id__in=search_query['department_permission'])
        else:
            items = Employers.objects.all()

        if search_query['name']:
            items = items.filter(fullname__icontains = search_query['name'])
        if search_query['department']:
            items = items.filter(department_id = search_query['department'])
        if search_query['shift']:
            if int(search_query['shift']) == 1:
                items = items.filter(shift_personnel=1)
            if int(search_query['shift']) == 2:
                items = items.filter(shift_personnel=0)
        if search_query['in_fired']:
            items = items.filter(fired=1)
        else:
            items = items.filter(fired=0)
        
        items.order_by('fullname')

        return items
    
def tabel_auto_fill(request, id):


    def CreateTabel(TabelArray):

        for data in TabelArray:

            

            

            newitem = TabelItem.objects.create(
                bound_tabel     = tabel,
                employer        = Employers.objects.get(id=data['id']),
                year            = tabel.year,
                month           = tabel.month,
                sHours24        = data['sHours24'],
                w_days          = data['w_days'],
                w_hours         = data['w_hours'],
                v_days          = data['v_days'],
                sHours19        = data['sHours19'],    
                sHours9         = data['sHours9'],     


            )

            for day in range(1, monthrange+1):
                tt  = 'type_time'   + str(day)
                h   = 'hours'       + str(day)

                setattr(newitem,    tt,    data[tt])
                setattr(newitem,    h,     data[h])
            
            newitem.save()
    pass        




    def TimeSummary(data):
    
        weekends_hours  = 0
        friday_hours    = 0
        work_hours      = 0
        work_days       = 0
        vacation_hours  = 0
        vacation_days   = 0
    
        for d in range(1, monthrange+1):
            if 'type_time' + str(d) in data:
                if data['type_time' + str(d)] in ['Я' ]:
                    work_hours      = work_hours + int(data['hours' + str(d)])
                    work_days       = work_days + 1
                
                if data['type_time' + str(d)] in ['Я/ЛЧ' ]:
                    friday_hours    = friday_hours + int(str(data['hours' + str(d)]).split('/')[1])
                    work_hours      = work_hours + int(str(data['hours' + str(d)]).split('/')[0])
                    work_days       = work_days + 1

                
                if data['type_time' + str(d)] in ['ОТ' ]:
                    vacation_hours  = vacation_hours + int(data['hours' + str(d)])
                    vacation_days   = vacation_days + 1
                
                if data['type_time' + str(d)] in ['В' ]: 
                    weekends_hours = weekends_hours + int(data['hours' + str(d)])

            totals = {
            'weekends_hours':    weekends_hours,
            'friday_hours':      friday_hours,
            'work_days':         work_days,
            'work_hours':        work_hours,
            'vacation_hours':    vacation_hours,
            'vacation_days':     vacation_days

        }   

        return totals

    
    tabel = TabelModel.objects.get(id=id)

    Employers_  = Employers.objects.filter(department=tabel.department_id).filter(fired=0).filter(shift_personnel=0).filter(mainworkplace=1) 
    
    
    if (len(tabel.month) == 2 and tabel.month[0] == 0):
        tabel_month = int(tabel.month[1])
    else:
        tabel_month = int(tabel.month)

    weekends    = []
    fridays     = []
    pre_celebs  = []
    TabelArray  = []

    monthrange = calendar.monthrange(int(tabel.year),tabel_month)
    monthrange = str(monthrange).split(',')[1]
    monthrange = int(str(monthrange).replace(' ','').replace(')',''))

    celebs = WorkCalendarRecord.objects.filter(year=tabel.year).filter(month=tabel_month)

    if celebs.count() == 1:
        celebs_in_str = str(celebs[0].days).split(',')
        celebs_in_int = []
        for c in celebs_in_str:
            celebs_in_int.append(int(c))
            if (int(c) - 1) > 0:
                pre_celebs.append(int(c) - 1) 
        celebs = celebs_in_int
    else:
        celebs = False




    for x in range(1, monthrange+1):
        day = calendar.weekday(2024,5,x)
        if day in [5,6]:
            weekends.append(x)
        if celebs:
            if x in celebs:
                weekends.append(x)
        if day in [4]:
            fridays.append(x)

    for e in Employers_:
            
        weekends_hours  = 0
        friday_hours    = 0
        work_hours      = 0
        work_days       = 0
        vacation_hours  = 0
        vacation_days   = 0

        TabelItems = TabelItem.objects.filter(employer_id=e.id).filter(bound_tabel_id=tabel.id)

        if TabelItems.count() == 0:
        
            vacation = vacshed_get_vacantions(request, e.id, tabel_month, tabel.year)
            js_vacation = json.loads(vacation.content)
            vacation = js_vacation[0]['days']
        

            data = {
                'id': e.id
            }

            for t in range(1, monthrange+1):
                tt = 'type_time' + str(t)
                data[tt] = 'Я' 
                h = 'hours' + str(t)
                data[h] = '8'


            if e.sex == 'Ж' :
                for f in fridays:
                    tt = 'type_time' + str(f)
                    data[tt] = 'Я/ЛЧ' 
                    h = 'hours' + str(f)
                    data[h] = '4/4'


            for w in weekends:
                tt = 'type_time' + str(w)
                data[tt] = 'В' 
                h = 'hours' + str(w)
                data[h] = '8'

            
            for p in pre_celebs:
                tt = 'type_time' + str(p)
                data[tt] = 'Я' 
                h = 'hours' + str(p)
                data[h] = '7'

            
            if len(vacation) > 0:

                for v in vacation:
                    tt = 'type_time' + str(v)
                    data[tt] = 'ОТ' 
                    h = 'hours' + str(v)
                    data[h] = '8'

   
                            
            totals = TimeSummary(data=data)

            data['sHours24']    = totals['weekends_hours']
            data['w_hours']     = totals['work_hours']
            data['w_days']      = totals['work_days']
            data['sHours19']    = totals['friday_hours']
            data['sHours9']     = totals['vacation_hours']
            data['v_days']      = totals['vacation_days']
            

            TabelArray.append(data)

    CreateTabel(TabelArray)

    return redirect('/turv/create/' + str(tabel.id))


    