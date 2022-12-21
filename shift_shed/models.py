from django.db import models



class ShiftShedModel(models.Model):
    year = models.CharField(verbose_name='Год', max_length=4, null=False, blank=False)
    dep = models.ForeignKey('TURV.department', verbose_name='Подразделение', on_delete=models.CASCADE)
    checked = models.BooleanField(verbose_name='Проверен', default=0)
    del_check = models.BooleanField(verbose_name='Пометка удаления', default=0)

    class Meta:
        verbose_name = 'График сменности'
        verbose_name_plural = 'Графики сменности'

    def __str__(self):
        return 'График сменности' + str(self.dep.name) + ' на ' + str(self.year) + 'г.'

class ShiftShedItem(models.Model):
    bound_shed = models.ForeignKey('ShiftShedModel', verbose_name='Св. график', db_index=True, on_delete=models.CASCADE)
    employer = models.ForeignKey('TURV.Employers', verbose_name='Сотрудник', db_index=True, on_delete=models.CASCADE)
    month = models.CharField(verbose_name='Месяц', db_index=True, max_length=256)



# Часы
    day_1 = models.CharField(max_length=4, verbose_name='День 1', null = True, blank=True)
    day_2 = models.CharField(max_length=4, verbose_name='День 2', null = True, blank=True)
    day_3 = models.CharField(max_length=4, verbose_name='День 3', null = True, blank=True)
    day_4 = models.CharField(max_length=4, verbose_name='День 4', null = True, blank=True)
    day_5 = models.CharField(max_length=4, verbose_name='День 5', null = True, blank=True)
    day_6 = models.CharField(max_length=4, verbose_name='День 6', null = True, blank=True)
    day_7 = models.CharField(max_length=4, verbose_name='День 7', null = True, blank=True)
    day_8 = models.CharField(max_length=4, verbose_name='День 8', null = True, blank=True)
    day_9 = models.CharField(max_length=4, verbose_name='День 9', null = True, blank=True)
    day_10 = models.CharField(max_length=4, verbose_name='День 10', null = True, blank=True)
    day_11 = models.CharField(max_length=4, verbose_name='День 11', null = True, blank=True)
    day_12 = models.CharField(max_length=4, verbose_name='День 12', null = True, blank=True)
    day_13 = models.CharField(max_length=4, verbose_name='День 13', null = True, blank=True)
    day_14 = models.CharField(max_length=4, verbose_name='День 14', null = True, blank=True)
    day_15 = models.CharField(max_length=4, verbose_name='День 15', null = True, blank=True)
    day_16 = models.CharField(max_length=4, verbose_name='День 16', null = True, blank=True)
    day_17 = models.CharField(max_length=4, verbose_name='День 17', null = True, blank=True)
    day_18 = models.CharField(max_length=4, verbose_name='День 18', null = True, blank=True)
    day_19 = models.CharField(max_length=4, verbose_name='День 19', null = True, blank=True)
    day_20 = models.CharField(max_length=4, verbose_name='День 20', null = True, blank=True)
    day_21 = models.CharField(max_length=4, verbose_name='День 21', null = True, blank=True)
    day_22 = models.CharField(max_length=4, verbose_name='День 22', null = True, blank=True)
    day_23 = models.CharField(max_length=4, verbose_name='День 23', null = True, blank=True)
    day_24 = models.CharField(max_length=4, verbose_name='День 24', null = True, blank=True)
    day_25 = models.CharField(max_length=4, verbose_name='День 25', null = True, blank=True)
    day_26 = models.CharField(max_length=4, verbose_name='День 26', null = True, blank=True)
    day_27 = models.CharField(max_length=4, verbose_name='День 27', null = True, blank=True)
    day_28 = models.CharField(max_length=4, verbose_name='День 28', null = True, blank=True)
    day_29 = models.CharField(max_length=4, verbose_name='День 29', null = True, blank=True)
    day_30 = models.CharField(max_length=4, verbose_name='День 30', null = True, blank=True)
    day_31 = models.CharField(max_length=4, verbose_name='День 31', null = True, blank=True)


#Итоги времени
    fact = models.FloatField(verbose_name='Факт. часов', help_text='Фактические часы', null = True, blank=True)
    celeb = models.FloatField(verbose_name='Праздничные', null = True, blank=True)


    class Meta:
        ordering = ['employer']
        verbose_name = 'Сотрудник в графике'
        verbose_name_plural = 'Сотрудники в графиках'

    def __str__(self):
        doc_fullname = str(self.employer) + ' ' + str(self.month) + '  ' + str(self.bound_shed.year)
        return doc_fullname
