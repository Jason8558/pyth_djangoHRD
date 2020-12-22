from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OutBoundDocument(models.Model):


    doc_type = models.CharField(default='Письмо', max_length=100, help_text="Введите вид документа (письмо, справка, и.т.д)", verbose_name='Вид', db_index=True)
    # doc_number = models.CharField(max_length=256, help_text="Введите номер документа", verbose_name='Номер документа', db_index=True)
    doc_date = models.DateField(help_text="Введите дату документа", verbose_name='Дата документа', db_index=True)
    doc_dest =  models.CharField(max_length=256, help_text="Введите адресата", verbose_name='Получатель (адресат)')
    doc_additionalData = models.CharField(default='none', max_length=256, help_text="Введите содержание документа", verbose_name='Содержание документа')
    doc_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящие документы'

    def __str__(self):
        doc_fullname = self.doc_type + ' №' + str(self.id) + ' от ' + str(self.doc_date)
        return doc_fullname

class LetterOfResignation(models.Model):

    lor_date = models.DateField(help_text="Введите дату поступления заявления", verbose_name="Дата поступления заявления", db_index=True)
    lor_employee = models.CharField(max_length=256, help_text="Введите ФИО увольняемого сотрудника", verbose_name="Увольняемый сотрудник")
    lor_position = models.CharField(max_length=256, help_text="Введите должность увольняемого сотрудника", verbose_name="Должность")
    lor_departament = models.CharField(max_length=256, help_text="Введите подразделение увольняемого сотрудника", verbose_name="Подразделение")
    lor_dateOfRes = models.DateField(help_text="Введите дату увольнения", verbose_name="Дата увольнения", db_index=True)
    lor_additionalData = models.CharField(blank=True, default="примечание", max_length=256, help_text="Введите примечание", verbose_name="Примечание")
    lor_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Заявление на увольнение'
        verbose_name_plural = 'Заявления на увольнение'

class LetterOfInvite(models.Model):
    loi_date = models.DateField(help_text="Введите дату поступления заявления", verbose_name="Дата поступления заявления", db_index=True)
    loi_employee = models.CharField(max_length=256, help_text="Введите ФИО принимаемого сотрудника", verbose_name="Принимаемый сотрудник")
    loi_position = models.CharField(max_length=256, help_text="Введите должность принимаемого сотрудника", verbose_name="Должность")
    loi_department = models.CharField(max_length=256, help_text="Введите подразделение принимаемого сотрудника", verbose_name="Подразделение")
    loi_dateOfInv = models.DateField(blank=True, null=True, help_text="Введите дату начала работы", verbose_name="Дата начала работы", db_index=True)
    loi_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Заявление на прием'
        verbose_name_plural = 'Заявления на прием'

class OrdersOnOtherMatters(models.Model):
    oom_number = models.CharField(max_length=5, help_text="Введите номер приказа", verbose_name="Номер приказа", db_index=True)
    oom_date = models.DateField(help_text="Введите дату приказа", verbose_name="Дата приказа", db_index=True)
    oom_content = models.CharField(max_length=256, help_text="Введите содержание приказа", verbose_name='Содержание')
    oom_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Приказ по другим вопросам'
        verbose_name_plural = 'Приказы по другим вопросам'

class OrdersOnVacation(models.Model):
    oov_number = models.CharField(max_length=8, help_text="Введите номер приказа", verbose_name="Номер приказа", db_index=True)
    oov_date = models.DateField(help_text="Введите дату приказа", verbose_name="Дата приказа", db_index=True)
    oov_empList = models.TextField(help_text="Введите сотрудников в приказ", verbose_name="Список сотрудников в приказе")
    oov_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Приказ на отпуск'
        verbose_name_plural = 'Приказы на отпуск'

class OrdersOfBTrip(models.Model):
    bt_number = models.CharField(max_length=5, help_text="Введите номер приказа", verbose_name="Номер приказа", db_index=True)
    bt_date = models.DateField(help_text="Введите дату приказа", verbose_name="Дата приказа", db_index=True)
    bt_dep = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name="Подразделение ", default="1")
    bt_place = models.CharField(max_length=256, help_text="Введите место командировки", verbose_name="Место командировки", db_index=True)
    bt_emloyer = models.CharField(max_length=256, help_text="Введите ФИО сотрудника", verbose_name="ФИО сотрудника", db_index=True)
    bt_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["bt_number"]
        verbose_name = 'Приказ о командировке'
        verbose_name_plural = 'Приказы о командировках'

    def __str__(self):
        doc_fullname = "Приказ о командировке" + ' №' + str(self.bt_number) + ' от ' + str(self.bt_date)
        return doc_fullname




class Departments(models.Model):
    dep_name = models.CharField(max_length=256, help_text="Введите название подразделения", verbose_name="Название подразделения", db_index=True)

    class Meta:
        ordering = ["dep_name"]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
    def __str__(self):
        doc_fullname = self.dep_name
        return doc_fullname
