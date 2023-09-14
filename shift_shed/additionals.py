from vac_shed.models import VacantionSheduleItem
from shift_shed.models import ShiftShedItem
from django.db.models import Avg, Count, Min, Sum
from TURV.models import Employers
import datetime
import calendar

def addition_sheditem(emps, year):
    months = []
    emps_vacs = list()
    for e in emps:
        if e != '':
            vacs_ = list()
            vacs = VacantionSheduleItem.objects.filter(emp_id=e).filter(bound_shed__year=year)

            for v in vacs:
                if (not v.move_from) and (not v.move_to):
                    vacs_.append({
                    'from':v.dur_from,
                    'to': v.dur_to
                    })
                else:
                    vacs_.append({
                    'from':v.move_from,
                    'to': v.move_to
                    })
            emps_vacs.append({
            'emp':e,
            'vacs':vacs_
            })

    vac_days = list()
    for rec in emps_vacs:

        emp = Employers.objects.get(id=rec['emp'])
        
        for vac in rec['vacs']:
            mfrom = datetime.datetime.strptime(str(vac['from']), "%Y-%m-%d").month
            mto = datetime.datetime.strptime(str(vac['to']), "%Y-%m-%d").month
            count = int(mto) - int(mfrom)


            end_day_from = calendar.monthrange(int(year),int(mfrom))
            end_day_to = datetime.datetime.strptime(str(vac['to']), "%Y-%m-%d").day
            first_day = datetime.datetime.strptime(str(vac['from']), "%Y-%m-%d").day
            from_days = []
            to_days = []

            if int(mfrom) < int(mto):
                for i in range(first_day,end_day_from[1]+1):
                    from_days.append(i)
                vac_days.append({
                'emp':emp,
                'month':mfrom,
                'days':from_days
                })

                for i in range(1,end_day_to+1):
                    to_days.append(i)
                vac_days.append({
                'emp':emp,
                'month':mto,
                'days':to_days
                })
            else:
                pass
            if int(mfrom) == int(mto):
                for i in range(first_day,end_day_from[1]+1):
                    from_days.append(i)
                vac_days.append({
                'emp':emp,
                'month':mfrom,
                'days':from_days
                })
    vac_days = sorted(vac_days, key=lambda x: x['emp'].id)

    for v in vac_days:
        print(v['emp'].fullname)


    return vac_days

def addition_shedform(id):
    items = ShiftShedItem.objects.filter(bound_shed_id=id)
    table_items = list()
    for item in items:
        days = list()
        days.append({
        '1':item.day_1,
        '2':item.day_2,
        '3':item.day_3,
        '4':item.day_4,
        '5':item.day_5,
        '6':item.day_6,
        '7':item.day_7,
        '8':item.day_8,
        '9':item.day_9,
        '10':item.day_10,
        '11':item.day_11,
        '12':item.day_12,
        '13':item.day_13,
        '14':item.day_14,
        '15':item.day_15,
        '16':item.day_16,
        '17':item.day_17,
        '18':item.day_18,
        '19':item.day_19,
        '20':item.day_20,
        '21':item.day_21,
        '22':item.day_22,
        '23':item.day_23,
        '24':item.day_24,
        '25':item.day_25,
        '26':item.day_26,
        '27':item.day_27,
        '28':item.day_28,
        '29':item.day_29,
        '30':item.day_30,
        '31':item.day_31


        })

        
        
        if item.celeb == None:
            celeb = '0,0'
        else:
            celeb = item.celeb
      
        table_items.append({
        'id': item.id,
        'employer':item.employer,
        'month':item.month,
        'fact':item.fact,
        'celeb':celeb,
        'norma':item.norma,
        'deviation':item.deviation,
        'days':days
        })

    return table_items

def addition_formforedit(id, month):
    items = ShiftShedItem.objects.filter(bound_shed_id=id).filter(month=month)
    edit_items = list()
    for item in items:
        days = list()
        days.append({
        '1':item.day_1,
        '2':item.day_2,
        '3':item.day_3,
        '4':item.day_4,
        '5':item.day_5,
        '6':item.day_6,
        '7':item.day_7,
        '8':item.day_8,
        '9':item.day_9,
        '10':item.day_10,
        '11':item.day_11,
        '12':item.day_12,
        '13':item.day_13,
        '14':item.day_14,
        '15':item.day_15,
        '16':item.day_16,
        '17':item.day_17,
        '18':item.day_18,
        '19':item.day_19,
        '20':item.day_20,
        '21':item.day_21,
        '22':item.day_22,
        '23':item.day_23,
        '24':item.day_24,
        '25':item.day_25,
        '26':item.day_26,
        '27':item.day_27,
        '28':item.day_28,
        '29':item.day_29,
        '30':item.day_30,
        '31':item.day_31
        })
        edit_items.append({
        'id':item.id,
        'employer':item.employer,
        'month':item.month,
        'fact':item.fact,
        'celeb':item.celeb,
        'days':days,
        'norma':item.norma,
        'deviation':item.deviation
        })

    return edit_items

def additional_formtotal(shed):
    emps = ShiftShedItem.objects.filter(bound_shed_id=shed).filter(month=1).values('employer').order_by('employer')
    total = list()
    for emp in emps:
        totals = ShiftShedItem.objects.filter(employer=emp['employer']).filter(bound_shed_id=shed).aggregate(s_fact=Sum('fact'), s_celeb=Sum('celeb'), s_norma=Sum('norma'), s_dev=Sum('deviation'))
        if totals['s_dev'] > 120 or totals['s_dev'] < 0:
            color = 'red'
        else:
            color = ''
        
        total.append({
            'emp':Employers.objects.get(id=emp['employer']),
            'color':color,
            's_fact':totals['s_fact'],
            's_celeb':totals['s_celeb'],
            's_norma':totals['s_norma'],
            's_dev':totals['s_dev']
        })
    return total
