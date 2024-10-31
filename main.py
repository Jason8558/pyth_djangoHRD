from move import *

com = input("Введите команду: ")

if com == 'vacshed':
    OldVs   = input('Введите ID старого графика: ')
    NewVs   = input('Введите ID нового графика: ') 
    move_from_vacshed(OldVs,NewVs)

elif com == 'move':
    OldDep  = input('Введите ID старого подразделения: ')
    NewDep  = input('Введите ID нового подразделения: ')
    Pos     = input('Введите ID должности: ')
    move_from_department(OldDep,NewDep,Pos)

else:
    print('Такой команды не существует')