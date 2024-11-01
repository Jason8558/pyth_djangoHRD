
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrd_docFlow.settings_local_workDB")
import django
django.setup()
from TURV.models import *
from vac_shed.models import *
from shift_shed.models import *
from django.db import connection
import json
import tkinter as tk
import io
from tkinter import filedialog as fd 




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
def move_from_department(NewDep):

    EmployersToMove = read_json()
    
    for Emp in EmployersToMove:
        EmpFromDb = get_employer_from_db(Emp)
        if EmpFromDb:
            OldId = Emp
            OldDep = EmpFromDb.department_id
            EmpFromDb.pk = None
            EmpFromDb.department = Department.objects.get(id=NewDep)
            EmpFromDb.save()

        cursor.execute("INSERT INTO move_employers(fullname,old_id,new_id,old_dep,new_dep) VALUES (%s,%s,%s,%s,%s)", [EmpFromDb.fullname, OldId, EmpFromDb.pk, OldDep, NewDep])

# 2. Переносим график отпусков
def move_from_vacshed(VsYear, NewVS):
    NewDep = VacantionShedule.objects.get(pk=NewVS).dep_id
    VSItems = VacantionSheduleItem.objects.filter(bound_shed__year = VsYear)

    for VSI in VSItems:
        cursor.execute("SELECT new_id FROM move_employers WHERE old_id=%s and new_dep=%s", [VSI.emp_id, NewDep])
        NewEmp = cursor.fetchone()
        if NewEmp:

            VSI.pk = None
            VSI.bound_shed = VacantionShedule.objects.get(pk=NewVS)
            VSI.emp = Employers.objects.get(pk=NewEmp[0])
            VSI.save()
        else:
            continue

# 3. Переносим график сменности
def move_from_shiftshed(SsYear, NewSS):
    NewDep  = ShiftShedModel.objects.get(pk=NewSS).dep_id
    SSItems = ShiftShedItem.objects.filter(bound_shed__year = str(SsYear))

    for SSI in SSItems:
        cursor.execute("SELECT new_id FROM move_employers WHERE old_id=%s and new_dep=%s", [SSI.employer_id, NewDep])
        NewEmp = cursor.fetchone()
        if NewEmp:

            SSI.pk = None
            SSI.bound_shed  = ShiftShedModel.objects.get(pk=NewSS)
            SSI.employer    = Employers.objects.get(pk=NewEmp[0])
            SSI.save()
        else:
            continue


# Вспомогательные функции

def read_json():

    name = fd.askopenfilename(title="Выберите файл с работниками") 
    
    JsonFile = io.open(name, encoding='utf-8', mode='r')
    try:
        JsonToCheck = json.load(JsonFile)
    except Exception:
        print('Ошибка чтения JSON: ' + Exception)
        exit()

    NamesToCompare = []

    for Emp in JsonToCheck:
        NamesToCompare.append(SetNameToCompare(Emp['name']))

    ComparedEmps = compare_with_db(NamesToCompare)

    return ComparedEmps

def compare_with_db(NamesToCompare: list):
    ComparedEmps = Employers.objects.filter(fullname__in = NamesToCompare).filter(fired=0).filter(mainworkplace=1)
    ComparedEmps = list(ComparedEmps.values_list('id', flat=True))
    
    return ComparedEmps

def SetNameToCompare(NameToComapre: str):
    NameSplit = NameToComapre.split(" ")
    for NS in NameSplit:
        if NS == "":
            NameSplit.pop(NameSplit.index(NS))
    
    NewNameToCompare = NameSplit[0] + " " + NameSplit[1][0] + "." + NameSplit[2][0] + "."

    return NewNameToCompare

def get_employer_from_db(id):
    Emps = Employers.objects.filter(id=id)
    if Emps:
        return Emps[0]
    else:
        return None


