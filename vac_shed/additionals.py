from .models import *
from TURV.models import *
from work_cal.models import WorkCalendarRecord
import calendar


def vacshed_get_vacantions(emp, month, year):
    v_items = VacantionSheduleItem.objects.filter(emp_id=emp).filter(bound_shed__year=year)
 
    emp_ = Employers.objects.get(id=emp)
    if emp_.sex == 'М':
        norm = Overtime.objects.get(year__year=year).value_m
    else:
        norm = Overtime.objects.get(year__year=year).value_w 



    days = list()
    vac_info = list()
    for item in v_items:
        if item.move_from:
            m_from      = int(str(item.move_from).split('-')[1])
            y_from      = int(str(item.move_from).split('-')[0])
            d_from      = int(str(item.move_from).split('-')[2])
        else:
            m_from      = int(str(item.dur_from).split('-')[1])
            y_from      = int(str(item.dur_from).split('-')[0])
            d_from      = int(str(item.dur_from).split('-')[2])
        
        if item.move_to:
            m_to        = int(str(item.move_to).split('-')[1])
            y_to        = int(str(item.move_to).split('-')[0]) 
            d_to        = int(str(item.move_to).split('-')[2])
        else:
            m_to        = int(str(item.dur_to).split('-')[1])
            y_to        = int(str(item.dur_to).split('-')[0]) 
            d_to        = int(str(item.dur_to).split('-')[2])

        
        
        
        
        if y_from == y_to: #если не переходит на след. год
            if m_to == m_from:
                if m_from == month:
                
                    for i in range(d_from, d_to+1):
                  
                        days.append(i)
            else:
                duration = m_to - m_from

                for i in range(m_from, m_to):
                    
                    if i == month and month != m_from and month != m_to:
                
                        for i in range (1, calendar.monthrange(int(year), int(month))[1]+1):
                            days.append(i)
            
                    if m_from == int(month):
                
                        m_end = calendar.monthrange(int(year), int(month))
                        for i in range (d_from, m_end[1]+1):
                            days.append(i)
                    
                    if m_to == int(month):
                
                        for i in range (1, d_to+1):
                            days.append(i)
        else:
            
            for i in range(m_from, 13):
                if i == month:

                    for day in range(d_from, calendar.monthrange(y_from, month)[1]+1):
                        days.append(day)
                    break
                # else:
                #     for day in range(1, calendar.monthrange(y_from, i)[1]+1):
                #         days.append(day)


   

                   
            
    vac_info.append({
        'emp':emp,
        'days':days,
        'norm':norm
    })

    return vac_info



