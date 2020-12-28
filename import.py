import pymysql
import xlrd
from contextlib import closing
from pymysql.cursors import DictCursor
connection = pymysql.connect(
    host='172.16.23.38',

    user='hrd_user',
    password='hrdpassword',
    db='hrd_docflow',
    charset='utf8mb4',
    cursorclass=DictCursor
)

# book1 = xlrd.open_workbook("deps.xlsx")
# sheet = book1.sheet_by_index(0)
# deps = sheet.col_values(0)



with connection.cursor() as cursor:
    query = 'select * FROM reg_jounals_departments '
    cursor.execute(query)
    for row in cursor:
        print(row)
    # connection.commit()
    # необходимо, т.к. по-умолчанию commit происходит только после выхода
    # из контекстного менеджера иначе мы бы не увидели твиттов
