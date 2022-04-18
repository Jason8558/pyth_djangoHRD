from django.db import models
from TURV.models import Employers as TEmps
from TURV.models import Department as TDeps


class VacantionShedule(models.Model):
    dep = models.ForeignKey('TURV.Department', verbose_name="Подразделение", on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="Период", db_index=True)
    res_officer = models.CharField(verbose_name="Ответственный", max_length=256, default='')
    class Meta:
        ordering = ['-year']
        verbose_name = 'График отпусков'
        verbose_name_plural = 'Графики отпусков'

    def __str__(self):
        name = 'График отпусков ' + self.dep.name + ' за ' + str(self.year) + ' год'
        return name

class VacantionSheduleItem(models.Model):
    bound_shed = models.ForeignKey('VacantionShedule', on_delete=models.CASCADE)
    emp = models.ForeignKey('TURV.Employers', on_delete = models.CASCADE, verbose_name="Сотрудник")
    dur_from = models.DateField(verbose_name="Период с")
    dur_to = models.DateField(verbose_name="Период по")
    days_count = models.IntegerField(verbose_name="Количество дней")
    class Meta:
        ordering = ['bound_shed']
        verbose_name = 'Элемент графика'
        verbose_name_plural = 'Элементы графика'
    def __str__(self):
        name = self.emp.fullname + ' ' +str(self.bound_shed.year)
        return name


# Create your models here.
