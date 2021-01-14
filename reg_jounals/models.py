from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OutBoundDocument(models.Model):


    doc_type = models.CharField(default='Письмо', max_length=100, help_text="Введите вид документа (письмо, справка, и.т.д)", verbose_name='Вид', db_index=True)
    doc_number = models.CharField(default='',max_length=10, help_text="Введите номер документа", verbose_name='Номер документа', db_index=True)
    doc_date = models.DateField(help_text="Введите дату документа", verbose_name='Дата документа', db_index=True)
    doc_dest =  models.CharField(max_length=256, help_text="Введите адресата", verbose_name='Получатель (адресат)')
    doc_additionalData = models.CharField(default='none', max_length=256, help_text="Введите содержание документа", verbose_name='Содержание документа')
    doc_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящие документы'

    def __str__(self):
        doc_fullname = self.doc_type + ' №' + str(self.doc_number) + ' от ' + str(self.doc_date)
        return doc_fullname

class LetterOfResignation(models.Model):

    lor_date = models.DateField(help_text="Введите дату поступления заявления", verbose_name="Дата поступления заявления", db_index=True)
    lor_number = models.CharField(default='',max_length=10, help_text="Введите номер документа", verbose_name='Номер документа', db_index=True)
    lor_employee = models.CharField(max_length=256, help_text="Введите ФИО увольняемого сотрудника", verbose_name="Увольняемый сотрудник")
    lor_position = models.CharField(max_length=256, help_text="Введите должность увольняемого сотрудника", verbose_name="Должность")
    lor_departament = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name="Подразделение ", default="1")
    lor_dateOfRes = models.DateField(help_text="Введите дату увольнения", verbose_name="Дата увольнения", db_index=True)
    lor_additionalData = models.CharField(blank=True, default="примечание", max_length=256, help_text="Введите примечание", verbose_name="Примечание")
    lor_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Заявление на увольнение'
        verbose_name_plural = 'Заявления на увольнение'

class LetterOfInvite(models.Model):
    loi_date = models.DateField(help_text="Введите дату поступления заявления", verbose_name="Дата поступления заявления", db_index=True)
    loi_number = models.CharField(default='',max_length=10, help_text="Введите номер документа", verbose_name='Номер документа', db_index=True)
    loi_employee = models.CharField(max_length=256, help_text="Введите ФИО принимаемого сотрудника", verbose_name="Принимаемый сотрудник")
    loi_position = models.CharField(max_length=256, help_text="Введите должность принимаемого сотрудника", verbose_name="Должность")
    loi_department = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name="Подразделение ", default="1")
    loi_dateOfInv = models.DateField(blank=True, null=True, help_text="Введите дату начала работы", verbose_name="Дата начала работы", db_index=True)
    loi_additionalData = models.CharField(blank=True, default="примечание", max_length=256, help_text="Введите примечание", verbose_name="Примечание")
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
    oov_number = models.CharField(blank = True, max_length=10, help_text="Введите номер приказа", verbose_name="Номер приказа", db_index=True)
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
    bt_dur_from = models.DateField(default='2000-01-01',help_text="Введите дату начала командировки", verbose_name="Дата начала командировки", db_index=True)
    bt_dur_to = models.DateField(default='2000-01-01',help_text="Введите дату завершения командировки", verbose_name="Дата завершения командировки", db_index=True)
    bt_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Приказ о командировке'
        verbose_name_plural = 'Приказы о командировках'

    def __str__(self):
        doc_fullname = "Приказ о командировке" + ' №' + str(self.bt_number) + ' от ' + str(self.bt_date)
        return doc_fullname

class OrdersOnPersonnel(models.Model):
    op_number = models.CharField(max_length=5, help_text="Введите номер приказа", verbose_name="Номер приказа", db_index=True)
    op_date = models.DateField(help_text="Введите дату приказа", verbose_name="Дата приказа", db_index=True)
    op_dep = models.ForeignKey('Departments', on_delete=models.CASCADE,  verbose_name="Подразделение ", default="1")
    op_emloyer = models.CharField(max_length=256, help_text="Введите ФИО сотрудника", verbose_name="ФИО сотрудника", db_index=True)
    op_content = models.TextField(help_text="Введите содержание", verbose_name="Содержание приказа")
    op_selected = models.BooleanField(verbose_name="Выделить в списке", default=False)
    op_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Приказ по личному составу'
        verbose_name_plural = 'Приказы по личному составу'

    def __str__(self):
        doc_fullname = "Приказ по личному составу" + ' №' + str(self.op_number) + ' от ' + str(self.op_date)
        return doc_fullname

class LaborContract(models.Model):
    lc_number = models.CharField(max_length=5, help_text="Введите номер договора", verbose_name="Номер договора", db_index=True)
    lc_date = models.DateField(help_text="Введите дату договора", verbose_name="Дата договора", db_index=True)
    lc_emloyer = models.CharField(max_length=256, help_text="Введите ФИО принимаемого сотрудника", verbose_name="ФИО принимаемого сотрудника", db_index=True)
    lc_pos = models.CharField(max_length=256, help_text="Введите должность", verbose_name="Должность", db_index=True, default=' ')
    lc_dep = models.ForeignKey('Departments', related_name="departments", on_delete=models.CASCADE, verbose_name="Подразделение ", default="1")
    lc_dateOfInv = models.DateField(help_text="Введите дату приема на работу", verbose_name="Дата приема на работу", db_index=True)
    lc_workCond = models.TextField(help_text="Введите условие работы", verbose_name="Условие работы", db_index=True)
    lc_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Трудовой договор'
        verbose_name_plural = 'Трудовые договоры'

    def __str__(self):
        doc_fullname = "Трудовой договор" + ' №' + str(self.lc_number) + ' от ' + str(self.lc_date)
        return doc_fullname

class EmploymentHistory(models.Model):
    eh_number = models.CharField(max_length=256, help_text="Введите номер трудовой книжки", verbose_name="Номер\серия", db_index=True)
    eh_dateOfInv = models.DateField(help_text="Введите дату приема на работу", verbose_name="Дата приема на работу", db_index=True)
    eh_employer = models.CharField(max_length=256, help_text="Введите ФИО принимаемого сотрудника", verbose_name="ФИО принимаемого сотрудника", db_index=True)
    eh_pos = models.CharField(max_length=256, help_text="Введите должность", verbose_name="Должность", db_index=True)
    eh_dep = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name="Подразделение ", default="79")
    eh_OrderInv = models.CharField(max_length=256, help_text="Введите номер приказа о приеме", verbose_name="Приказ о приеме на работу:", db_index=True)
    eh_OrderResign = models.CharField(null=True, blank=True, max_length=256, help_text="Введите номер приказа об увольнении", verbose_name="Приказ об увольнении:", db_index=True)
    eh_dateOfResign = models.DateField(null=True, blank=True, help_text="Введите дату увольнения", verbose_name="Дата увольнения", db_index=True)
    eh_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который внес документ в систему ", verbose_name='Ответственный сотрудник')

class SickRegistry(models.Model):
    sr_number = models.IntegerField(help_text="Введите номер реестра", verbose_name="Номер реестра", db_index=True)
    sr_res_officer = models.CharField(blank=True, editable=False,  max_length=256, help_text="Сотрудник, который создал реестр ", verbose_name='Ответственный сотрудник')

    class Meta:
        ordering = ["sr_number"]
        verbose_name = 'Реестр больничных листов'
        verbose_name_plural = 'Реестры больничных листов'
    def __str__(self):
        reg_num = str(self.sr_number)
        return reg_num
class SickDocument(models.Model):
    sd_reg_number = models.CharField(max_length=256, blank=True, help_text="Введите номер реестра", verbose_name="№ реестра ", default=" ")
    sd_number = models.CharField(max_length=256, help_text="Введите номер б\л", verbose_name="Номер б\л", db_index=True)
    sd_emp = models.CharField(max_length=256, help_text="Введите ФИО сотрудника", verbose_name="ФИО", db_index=True)
    sd_pos = models.CharField(max_length=256, help_text="Введите должность", verbose_name="Должность", db_index=True)
    sd_dep = models.ForeignKey('Departments',  on_delete=models.CASCADE, verbose_name="Подразделение ", default="1")
    sd_dur_from = models.DateField(help_text="Введите дату начала болезни", verbose_name="Дата начала болезни", db_index=True)
    sd_dur_to = models.DateField(help_text="Введите дату окончания болезни", verbose_name="Дата окончания болезни", db_index=True)
    sd_comm = models.CharField(blank=True, default=" ", max_length=256, help_text="Введите примечание", verbose_name="Примечание")

    class Meta:
        ordering = ["sd_reg_number"]
        verbose_name = 'Больничный лист'
        verbose_name_plural = 'Больничные листы'

    def __str__(self):
        doc_name = 'Больничный № ' + str(self.sd_number) + ' в реестре № ' + str(self.sd_reg_number)
        return doc_name

class Departments(models.Model):
    dep_name = models.CharField(max_length=256,  help_text="Введите название подразделения", verbose_name="Название подразделения", db_index=True)

    class Meta:
        ordering = ["dep_name"]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
    def __str__(self):
        doc_fullname = self.dep_name
        return doc_fullname
