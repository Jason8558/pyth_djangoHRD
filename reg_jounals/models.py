from django.db import models

# Create your models here.

class OutBoundDocument(models.Model):
    doc_name = models.CharField(max_length=100, help_text="Введите название документа", verbose_name='Название', db_index=True)
    doc_number = models.CharField(max_length=256, help_text="Введите номер документа", verbose_name='Номер документа', db_index=True)
    doc_date = models.DateField(help_text="Введите дату документа", verbose_name='Дата документа', db_index=True)
    doc_dest =  models.CharField(max_length=256, help_text="Введите адресата", verbose_name='Получатель (адресат)')
    doc_additionalData = models.CharField(max_length=256, blank=True ,help_text="Введите дополнительную информацию по документу (необязательно)", verbose_name='Дополнительная информация')
    doc_reg_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-doc_reg_date"]
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящие документы'


    def __str__(self):
        doc_fullname = self.doc_name + ' №' + str(self.doc_number) + ' от ' + str(self.doc_reg_date)
        return doc_fullname
