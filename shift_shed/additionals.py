from vac_shed.models import VacantionSheduleItem
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
        print(getattr(emp,'fullname'))
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


    return vac_days
