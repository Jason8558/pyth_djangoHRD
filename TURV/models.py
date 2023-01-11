from django.db import models
from django.contrib.auth.models import User
import datetime

class Employers(models.Model):
    sex_choices = [('М','М'),('Ж','Ж')]
    fullname = models.CharField(verbose_name = 'ФИО сотрудника', db_index=True, max_length=256)
    sex = models.CharField(verbose_name = 'Пол', choices=sex_choices, db_index=True, max_length=1, default="М")
    position = models.ForeignKey('Position', verbose_name='Должность', db_index=True, on_delete=models.CASCADE)
    shift_personnel = models.BooleanField(verbose_name='Сменный персонал', default=False)
    fired = models.BooleanField(verbose_name='Сотрудник уволен', default=False)
    stand_worktime = models.FloatField(verbose_name='Норма часов', default=0)
    department = models.ForeignKey('Department', verbose_name='Подразделение', on_delete=models.CASCADE)
    level = models.CharField(verbose_name='Разряд/категория', max_length=256)
    positionOfPayment = models.CharField(verbose_name='Ступень оплаты', max_length=3)
    mainworkplace = models.BooleanField(verbose_name='Основная специальность', default=True, blank=True)
    aup = models.ForeignKey('Department', verbose_name='Подчиненное подразделение', related_name="dep_aup", blank=True, null=True, default="", on_delete=models.CASCADE)

    class Meta:
        ordering = ['fullname']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return  self.fullname + ',' + str(self.position) + ',' + str(self.level) + ',' + str(self.positionOfPayment) + ',' + str(self.id) + ',' + str(self.shift_personnel) + ',' + str(self.stand_worktime) + ',' + str(self.sex)
        # return self.fullname

class Department(models.Model):
    name = models.CharField(verbose_name = 'Название подразделения', db_index=True, max_length=256)
    user = models.ManyToManyField(User, verbose_name = 'Табельщик')
    conftype = models.ManyToManyField('TabelType', verbose_name='Виды табелей для подразделения: ')
    onescode = models.CharField(verbose_name= 'Код подразделения в 1С ',  max_length=256, blank=True, null=True)
    is_aup = models.BooleanField(default=False)
    notused = models.BooleanField(default=False)
    shift = models.BooleanField(verbose_name="Подразделение содержит сменщиков", default=False)
    is_filial = models.BooleanField(default=False)
    dir = models.ForeignKey('Direction', verbose_name="Дирекция ", db_index=True, on_delete=models.CASCADE, blank=True, null=True, default='')
    union = models.ForeignKey('Union', verbose_name="Объединение ", db_index=True, on_delete=models.CASCADE, blank=True, null=True, default='')

    class Meta:
        ordering = ['name']
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name

class Direction(models.Model):
    name = models.CharField(verbose_name = 'Название дирекции', db_index=True, max_length=256)

    class Meta:
        ordering = ['name']
        verbose_name = 'Дирекция'
        verbose_name_plural = 'Дирекции'

    def __str__(self):
        return self.name

class Union(models.Model):
    name = models.CharField(verbose_name = 'Название объединения', db_index=True, max_length=256)

    class Meta:
        ordering = ['name']
        verbose_name = 'Объединение'
        verbose_name_plural = 'Объединения'

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(verbose_name = 'Название должности', db_index=True, max_length=256)

    class Meta:
        ordering = ['name']
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name

class Automobile(models.Model):
    number = models.CharField(verbose_name='Номер а\м',  db_index=True, max_length=256)
    model = models.CharField(verbose_name='Модель(необязательно) ',  max_length=256, blank=True, null=True)
    unite_p = models.IntegerField(verbose_name='Процент доплаты')
    used = models.BooleanField(verbose_name='Автомобиль используется', default=1)
    class Meta:
        ordering = ['unite_p']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
    def __str__(self):
        return self.number + "(" + str(self.unite_p) + ")"

class TabelType(models.Model):
    name = models.CharField(verbose_name='Вид табеля ',  max_length=256)
    class Meta:
        ordering = ['id']
        verbose_name = "Вид табеля"
        verbose_name_plural = "Виды табеля"
    def __str__(self):
        return self.name

class Tabel(models.Model):
    type = models.ForeignKey('TabelType', verbose_name="Вид ", db_index=True, on_delete=models.CASCADE, default='1')
    year = models.CharField(verbose_name='Год', db_index=True, max_length=4)
    month = models.CharField(verbose_name='Месяц', db_index=True, max_length=256)
    day = models.CharField(verbose_name='Число', db_index=True, max_length=256, blank=True, null=True, default="0")
    department = models.ForeignKey('Department', verbose_name=' ', db_index=True, on_delete=models.CASCADE)
    del_check = models.BooleanField(verbose_name='Пометка удаления', default=False, blank=True)
    sup_check = models.BooleanField(verbose_name='Проверен СУП', default=False, blank=True)
    paper_check = models.BooleanField(verbose_name='Сдан в бумажном виде',default=False)
    unloaded =  models.BooleanField(verbose_name='Загружен в 1С', default=False, blank=True)
    comm = models.CharField(verbose_name='Комментарий (НЕОБЯЗАТЕЛЬНО)', max_length=256, default="", blank=True)
    iscorr = models.BooleanField(default=False)
    corr = models.ForeignKey('Tabel', verbose_name="Корректировка к ", db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    half_month_check = models.BooleanField(verbose_name='Половина месяца заполнена', default=False, blank=True) 

    res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Отвественный за составление табеля", verbose_name='Табельщик')
    class Meta:
        ordering = ['-year']
        verbose_name = 'Табель'
        verbose_name_plural = 'Табели'

    def __str__(self):
        return str(self.department) + str(self.month) + str(self.year) + str(self.type.name)

class TabelItem(models.Model):
    bound_tabel = models.ForeignKey('Tabel', verbose_name='Св. табель', db_index=True, on_delete=models.CASCADE)
    employer = models.ForeignKey('Employers', verbose_name='Сотрудник', db_index=True, on_delete=models.CASCADE)
    year = models.CharField(verbose_name='Год', db_index=True, max_length=256)
    month = models.CharField(verbose_name='Месяц', db_index=True, max_length=256)
    toxic_p = models.IntegerField(blank=True, null=True, default=0, verbose_name='Процент доплаты за вредность')
    auto = models.ForeignKey('Automobile', verbose_name='а/м', on_delete=models.CASCADE, default='', blank=True, null=True)


# Виды времени
    type_time1 = models.CharField(max_length=4, verbose_name='Вид времени1', null = True, blank=True)
    type_time2 = models.CharField(max_length=4, verbose_name='Вид времени2', null = True, blank=True)
    type_time3 = models.CharField(max_length=4, verbose_name='Вид времени3', null = True, blank=True)
    type_time4 = models.CharField(max_length=4, verbose_name='Вид времени4', null = True, blank=True)
    type_time5 = models.CharField(max_length=4, verbose_name='Вид времени5', null = True, blank=True)
    type_time6 = models.CharField(max_length=4, verbose_name='Вид времени6', null = True, blank=True)
    type_time7 = models.CharField(max_length=4, verbose_name='Вид времени7', null = True, blank=True)
    type_time8 = models.CharField(max_length=4, verbose_name='Вид времени8', null = True, blank=True)
    type_time9 = models.CharField(max_length=4, verbose_name='Вид времени9', null = True, blank=True)
    type_time10 = models.CharField(max_length=4, verbose_name='Вид времени10', null = True, blank=True)
    type_time11 = models.CharField(max_length=4, verbose_name='Вид времени11', null = True, blank=True)
    type_time12 = models.CharField(max_length=4, verbose_name='Вид времени12', null = True, blank=True)
    type_time13 = models.CharField(max_length=4, verbose_name='Вид времени13', null = True, blank=True)
    type_time14 = models.CharField(max_length=4, verbose_name='Вид времени14', null = True, blank=True)
    type_time15 = models.CharField(max_length=4, verbose_name='Вид времени15', null = True, blank=True)
    type_time16 = models.CharField(max_length=4, verbose_name='Вид времени16', null = True, blank=True)
    type_time17 = models.CharField(max_length=4, verbose_name='Вид времени17', null = True, blank=True)
    type_time18 = models.CharField(max_length=4, verbose_name='Вид времени18', null = True, blank=True)
    type_time19 = models.CharField(max_length=4, verbose_name='Вид времени19', null = True, blank=True)
    type_time20 = models.CharField(max_length=4, verbose_name='Вид времени20', null = True, blank=True)
    type_time21 = models.CharField(max_length=4, verbose_name='Вид времени21', null = True, blank=True)
    type_time22 = models.CharField(max_length=4, verbose_name='Вид времени22', null = True, blank=True)
    type_time23 = models.CharField(max_length=4, verbose_name='Вид времени23', null = True, blank=True)
    type_time24 = models.CharField(max_length=4, verbose_name='Вид времени24', null = True, blank=True)
    type_time25 = models.CharField(max_length=4, verbose_name='Вид времени25', null = True, blank=True)
    type_time26 = models.CharField(max_length=4, verbose_name='Вид времени26', null = True, blank=True)
    type_time27 = models.CharField(max_length=4, verbose_name='Вид времени27', null = True, blank=True)
    type_time28 = models.CharField(max_length=4, verbose_name='Вид времени28', null = True, blank=True)
    type_time29 = models.CharField(max_length=4, verbose_name='Вид времени29', null = True, blank=True)
    type_time30 = models.CharField(max_length=4, verbose_name='Вид времени30', null = True, blank=True)
    type_time31 = models.CharField(max_length=4, verbose_name='Вид времени31', null = True, blank=True)

# Кол-ва часов
    hours1 = models.CharField(max_length=10, verbose_name='Часы1', null = True, blank=True)
    hours2 = models.CharField(max_length=10, verbose_name='Часы2', null = True, blank=True)
    hours3 = models.CharField(max_length=10, verbose_name='Часы3', null = True, blank=True)
    hours4 = models.CharField(max_length=10, verbose_name='Часы4', null = True, blank=True)
    hours5 = models.CharField(max_length=10, verbose_name='Часы5', null = True, blank=True)
    hours6 = models.CharField(max_length=10, verbose_name='Часы6', null = True, blank=True)
    hours7 = models.CharField(max_length=10, verbose_name='Часы7', null = True, blank=True)
    hours8 = models.CharField(max_length=10, verbose_name='Часы8', null = True, blank=True)
    hours9 = models.CharField(max_length=10, verbose_name='Часы9', null = True, blank=True)
    hours10 = models.CharField(max_length=10, verbose_name='Часы10', null = True, blank=True)
    hours11 = models.CharField(max_length=10, verbose_name='Часы11', null = True, blank=True)
    hours12 = models.CharField(max_length=10, verbose_name='Часы12', null = True, blank=True)
    hours13 = models.CharField(max_length=10, verbose_name='Часы13', null = True, blank=True)
    hours14 = models.CharField(max_length=10, verbose_name='Часы14', null = True, blank=True)
    hours15 = models.CharField(max_length=10, verbose_name='Часы15', null = True, blank=True)
    hours16 = models.CharField(max_length=10, verbose_name='Часы16', null = True, blank=True)
    hours17 = models.CharField(max_length=10, verbose_name='Часы17', null = True, blank=True)
    hours18 = models.CharField(max_length=10, verbose_name='Часы18', null = True, blank=True)
    hours19 = models.CharField(max_length=10, verbose_name='Часы19', null = True, blank=True)
    hours20 = models.CharField(max_length=10, verbose_name='Часы20', null = True, blank=True)
    hours21 = models.CharField(max_length=10, verbose_name='Часы21', null = True, blank=True)
    hours22 = models.CharField(max_length=10, verbose_name='Часы22', null = True, blank=True)
    hours23 = models.CharField(max_length=10, verbose_name='Часы23', null = True, blank=True)
    hours24 = models.CharField(max_length=10, verbose_name='Часы24', null = True, blank=True)
    hours25 = models.CharField(max_length=10, verbose_name='Часы25', null = True, blank=True)
    hours26 = models.CharField(max_length=10, verbose_name='Часы26', null = True, blank=True)
    hours27 = models.CharField(max_length=10, verbose_name='Часы27', null = True, blank=True)
    hours28 = models.CharField(max_length=10, verbose_name='Часы28', null = True, blank=True)
    hours29 = models.CharField(max_length=10, verbose_name='Часы29', null = True, blank=True)
    hours30 = models.CharField(max_length=10, verbose_name='Часы30', null = True, blank=True)
    hours31 = models.CharField(max_length=10, verbose_name='Часы31', null = True, blank=True)

#Итоги видов времени
    sHours1 = models.FloatField(verbose_name='Явки (Я)', help_text='Явки', null = True, blank=True)
    sHours2 = models.FloatField(verbose_name='Ночные (Н)', null = True, blank=True)
    sHours3 = models.FloatField(verbose_name='Работа в выходные и празд. (РВ)', null = True, blank=True)
    sHours4 = models.FloatField(verbose_name='Сверхурочные (С)', null = True, blank=True)
    sHours5 = models.IntegerField(verbose_name='Вахтовый метод (ВМ)', null = True, blank=True)
    sHours6 = models.IntegerField(verbose_name='Служебная командировка (К)', null = True, blank=True)
    sHours7 = models.IntegerField(verbose_name='Повыш. квалификации с отрывом от работы (ПК)', null = True, blank=True)
    sHours8 = models.IntegerField(verbose_name='Повыш. квалификации с отрывом от рб. в другой мес-ти (ПМ)', null = True, blank=True)
    sHours9 = models.IntegerField(verbose_name='Основной оплачиваемый отпуск (ОТ)', null = True, blank=True)
    sHours10 = models.IntegerField(verbose_name='Дополнительный оплачиваемый отпуск (ОД)', null = True, blank=True)
    sHours11 = models.IntegerField(verbose_name='Учебный отпуск (У)', null = True, blank=True)
    sHours12 = models.IntegerField(verbose_name='Сокращенная продолжительность для обучающихся без отрыва (УВ)', null = True, blank=True)
    sHours13 = models.IntegerField(verbose_name='Неоплачиваемый учебный отпуск (УД)', null = True, blank=True)
    sHours14 = models.IntegerField(verbose_name='Отпуск по беременности и родам (Р)', null = True, blank=True)
    sHours15 = models.IntegerField(verbose_name='Отпуск по уходу за ребенком до 3-х лет (ОЖ)', null = True, blank=True)
    sHours16 = models.IntegerField(verbose_name='Отпуск без сохр. зп по разрешению работодателя (ДО)', null = True, blank=True)
    sHours17 = models.IntegerField(verbose_name='Временная нетрудоспособность (Б)', null = True, blank=True)
    sHours18 = models.IntegerField(verbose_name='Неоплачиваемый больничный (Т)', null = True, blank=True)
    sHours19 = models.IntegerField(verbose_name='Сокращенная продолжительность рабочего времени (ЛЧ)', null = True, blank=True)
    sHours20 = models.IntegerField(verbose_name='Время вынужденного прогула в случае признания увольнения незаконным (ПВ)', null = True, blank=True)
    sHours21 = models.IntegerField(verbose_name='Невыходы на время исполнения гос. ил общ. обязанностей (Г)', null = True, blank=True)
    sHours22 = models.IntegerField(verbose_name='Прогулы (ПР)', null = True, blank=True)
    sHours23 = models.IntegerField(verbose_name='Работа в режиме неполного рабочего времени (НС)', null = True, blank=True)
    sHours24 = models.FloatField(verbose_name='Выходные (В)', null = True, blank=True)
    sHours25 = models.IntegerField(verbose_name='Дополнительные выходные оплачиваемые (ОВ)', null = True, blank=True)
    sHours26 = models.IntegerField(verbose_name='Дополнительные выходные неоплачиваемые (НВ)', null = True, blank=True)
    sHours27 = models.IntegerField(verbose_name='Забастовка (ЗБ)', null = True, blank=True)
    sHours28 = models.IntegerField(verbose_name='Неявки по невыясненным причинам (НН)', null = True, blank=True)
    sHours29 = models.IntegerField(verbose_name='Время простоя по вине работодателя (РП)', null = True, blank=True)
    sHours30 = models.IntegerField(verbose_name='Время простоя по причинам, не зависищим от работника и работодателя (НП)', null = True, blank=True)
    sHours31 = models.IntegerField(verbose_name='Время простоя по вине работника (ВП)', null = True, blank=True)
    sHours32 = models.IntegerField(verbose_name='Оплачиваемое отстранение от работы (НО)', null = True, blank=True)
    sHours33 = models.IntegerField(verbose_name='Неоплачиваемое отстранение от работы (НБ)', null = True, blank=True)
    sHours34 = models.IntegerField(verbose_name='Остановка работы про причине невыплаты ЗП (НЗ)', null = True, blank=True)
    sHours35 = models.IntegerField(verbose_name='Совмещение', null = True, blank=True)
    sHours36 = models.IntegerField(verbose_name='Местная командировка', null = True, blank=True)
    sHours37 = models.IntegerField(verbose_name='Пенсионный', null = True, blank=True)
    sHours38 = models.IntegerField(verbose_name='Нерабочие оплачиваемые дни', null = True, blank=True)
    sHours39 = models.IntegerField(verbose_name='Отсутствие по мобилизации', null = True, blank=True)
    w_days = models.IntegerField(verbose_name='Дней отработано', default=0, null = True, blank=True)
    # w_hours = models.IntegerField(verbose_name='Часов отработано', default=0, null = True, blank=True)
    w_hours = models.FloatField(verbose_name='Часов отработано', default=0, null = True, blank=True)
    v_days = models.IntegerField(verbose_name='Дней неявок', default=0, null = True, blank=True)
    # v_hours = models.IntegerField(verbose_name='Часов неявок', default=0, null = True, blank=True)
    v_hours = models.FloatField(verbose_name='Часов неявок', default=0, null = True, blank=True)

    class Meta:
        ordering = ['-year']
        verbose_name = 'Сотрудник в табеле'
        verbose_name_plural = 'Сотрудники в табелях'

    def __str__(self):
        doc_fullname = str(self.employer) + ' ' + str(self.month) + '  ' + str(self.year)
        return doc_fullname

class Category(models.Model):
    name = models.CharField(verbose_name='Наименование ', max_length=4)
    class Meta:
        ordering = ["id"]
        verbose_name = 'Категория'

    def __str__(self):
        fullname = self.name
        return fullname


class Overtime(models.Model):
    year = models.DateField(verbose_name='Период', db_index=True)
    value_m = models.FloatField(verbose_name='Значение_мужчины', default=0)
    value_w = models.FloatField(verbose_name='Значение_женщины', default=0)

    class Meta:
        ordering = ['-year']
        verbose_name = 'Норма времени'
        verbose_name_plural = 'Нормы врмени'

    def __str__(self):
        fullname = str(self.year)
        return fullname

class InfoMessages(models.Model):
        class ViewInCHS(models.TextChoices):
            mainw = '1','Главное окно'
            intabel = '2', 'Окно табеля'
            edit = '3', 'Окно редактирования табеля'

        class MesTypeCHS(models.TextChoices):
            ord = '1','Обычное'
            vac = '2', 'О переносе отпуска'

        text = models.TextField(verbose_name='Текст сообщения: ', blank=False, null=False)
        alldeps = models.BooleanField(default=True, verbose_name='Для всех')
        deps = models.ManyToManyField('Department', null=True, blank=True, verbose_name='Подразделения, для которых предназначена информация: ')
        active = models.BooleanField(default=True, verbose_name='Сообщение активно')
        dfrom = models.DateField(verbose_name='Дата начала показа: ', null=True, blank=True)
        dto = models.DateField(verbose_name='Дата окончания показа: ', null=True, blank=True)
        always = models.BooleanField(default=True, verbose_name='Показывать постоянно')
        viewin = models.CharField(max_length=100, choices=ViewInCHS.choices, default=ViewInCHS.mainw)
        alltypes = models.BooleanField(verbose_name='Для всех видов табеля',default=True)
        intypes = models.ManyToManyField('TabelType', verbose_name="Отображать в табелях: ", default='1')
        mestype = models.CharField(max_length=100, choices=MesTypeCHS.choices, default=MesTypeCHS.ord)
        important = models.BooleanField(default=False, verbose_name='Особо важное')

        class Meta:
            ordering = ['-id']
            verbose_name = "Сообщение пользователям"
            verbose_name_plural = "Система оповещения пользователей"

class FeedBackTypes(models.Model):
    name = models.CharField(blank=False, null=False, verbose_name='Наименование', max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Вид сообщения'
        verbose_name = 'Виды сообщений от пользователей'

    def __str__(self):
        return str(self.name)

class FeedBack(models.Model):
    mes_from = models.ForeignKey(User, verbose_name='От кого', db_index=True, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    about = models.CharField(blank=False,null=False, verbose_name='Тема', max_length=100)
    text = models.TextField(blank=False, null=False, verbose_name='Текст сообщения')
    type = models.ForeignKey('FeedBackTypes', on_delete=models.CASCADE, verbose_name='Вид сообщения')
    inwork = models.BooleanField(default=False, verbose_name='Принято в работу')
    readed = models.BooleanField(default=False, verbose_name='Прочитано')
    answer = models.TextField(blank=True, null=True, verbose_name='Ответ на сообщение')
    answer_readed = models.BooleanField(default=False, verbose_name='Ответ прочитан')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = 'Сообщения пользователей'
