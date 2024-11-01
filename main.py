from move import *

com = input("Введите команду: ")

if com == 'vacshed':
    VsYear   = input('Год старых графиков: ')
    NewVs   = input('Введите ID нового графика: ') 
    move_from_vacshed(VsYear,NewVs)

elif com == 'move':
    OldDep  = input('Введите ID старого подразделения: ')
    NewDep  = input('Введите ID нового подразделения: ')
    # Pos     = input('Введите ID должности: ')
    move_from_department(OldDep,NewDep)

elif com == 'shiftshed':
    print('Перенос графика сменности')
    SsYear   = input('Год старых графиков: ')
    NewSS   = input('Введите ID нового графика: ') 
    move_from_shiftshed(SsYear,NewSS)
elif com == 'json':
    read_json()
else:
    print('Такой команды не существует')