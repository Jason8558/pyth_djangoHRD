from TURV.models import Department as Departments
from TURV.models import Position as Positions
from TURV.models import Employers
from TURV.models import Overtime 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import datetime as DT

@login_required
def create_or_update_employer(emp_id:int, emp_info:dict):

   
    fullname        = emp_info['fullname']
    position        = Positions.objects.get(id=emp_info['position'])
    department      = Departments.objects.get(id=emp_info['department'])
    sex             = emp_info['sex']
    shift           = emp_info['shift']
    level           = emp_info['level']
    payment_level   = emp_info['payment_level']

    if int(emp_info['sub_department']) == 0:
        sub_department  = None
    else:
        sub_department  = Departments.objects.get(id=emp_info['sub_department'])

    if int(shift) == 1:
        # Данные о норме времени для сменщиков
        year_ = str(DT.datetime.now().year) + "-01-01"
   
        work_time = Overtime.objects.get(year=year_)

        if sex == "М":
            work_time_limit = work_time.value_m
        else:
            # Женщины
            work_time_limit = work_time.value_w

    else:
        work_time_limit = 0

    if emp_id == 0:

        new_emp = Employers.objects.create(
            fullname            = fullname,
            sex                 = sex,
            level               = level,
            positionOfPayment   = payment_level,
            department          = department,
            aup                 = sub_department,
            position            = position,
            shift_personnel     = shift,
            stand_worktime      = work_time_limit,

        )
    else:
        new_emp = Employers.objects.get(id=emp_id)

        new_emp.fullname            = fullname
        new_emp.sex                 = sex
        new_emp.level               = level
        new_emp.positionOfPayment   = payment_level
        new_emp.department          = department
        new_emp.aup                 = sub_department
        new_emp.position            = position
        new_emp.shift_personnel     = shift
        new_emp.stand_worktime      = work_time_limit


    new_emp.save()

    return new_emp

@login_required
def get_employers_from_department(request, department_id:int):
    employers = Employers.objects.filter(fired=0).filter(mainworkplace=1).filter(department_id=department_id).order_by('fullname').values('id', 'fullname')
    employers = list(employers)
    
    return JsonResponse(employers, safe=False)