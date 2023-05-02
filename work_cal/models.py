from django.db import models

class WorkCalendarRecord(models.Model):
    year = models.CharField(max_length=4, verbose_name='Год', blank=False, null=False)
    month = models.IntegerField(verbose_name='Месяц', blank=False, null=False)
    days = models.CharField(verbose_name='Дни', max_length=256, blank=True, null=False)

    class Meta:
        verbose_name = 'Запись в календаре'
        verbose_name_plural = 'Производственный календарь'

    def __str__(self):
        return self.year + " " + str(self.month)
