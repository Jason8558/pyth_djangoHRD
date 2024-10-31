# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrd_docFlow.settings_local")
import django
django.setup()
from TURV.models import *
from vac_shed.models import *
from django.db import connection
import json


# Старое подразделение
# OldDep = 18 
# # Новое подразделение
# NewDep = 69
# # Старый график отпусков 
# OldVS  = 87
# # Новый график отпусков
# NewVS  = 115
# # 
# Pos    = 147

cursor = connection.cursor()
#  you have to set the correct path to you settings module

# with connection.cursor() as cursor:
#     cursor.execute("SELECT fullname FROM TURV_employers ORDER BY fullname")
#     res = cursor.fetchall()
#     for r in res:
#         print(r[0])

# 1. Собрать работников КИП, которые не уволены, и у которых основное рабочее место
def move_from_department(OldDep, NewDep, Pos):

    kip = Employers.objects.filter(department_id=OldDep).filter(fired=0).filter(mainworkplace=1)
    if Pos:
        kip = kip.filter(position_id=Pos)
    
    for k in kip:
        OldId = k.pk
        k.pk = None
        k.department = Department.objects.get(id=NewDep)
        k.save()

        cursor.execute("INSERT INTO move_employers(old_id,new_id,old_dep,new_dep) VALUES (%s,%s,%s,%s)", [OldId, k.id, OldDep, NewDep])

# 2. Переносим график отпусков
def move_from_vacshed(OldVS, NewVS):
    VSItems = VacantionSheduleItem.objects.filter(bound_shed = OldVS)

    for VSI in VSItems:
        cursor.execute("SELECT new_id FROM move_employers WHERE old_id=%s", [VSI.emp_id])
        NewEmp = cursor.fetchone()
        if NewEmp:

            VSI.pk = None
            VSI.bound_shed = VacantionShedule.objects.get(pk=NewVS)
            VSI.emp = Employers.objects.get(pk=NewEmp[0])
            VSI.save()
        else:
            continue



