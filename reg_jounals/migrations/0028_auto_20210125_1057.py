# Generated by Django 3.1.2 on 2021-01-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0027_auto_20210125_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newordersonvacation_item',
            name='vac_type',
            field=models.CharField(choices=[('Очередной', 'Очередной'), ('Пенсионный', 'Пенсионный'), ('Без сохранения ЗП', 'Без сохранения ЗП'), ('Учебный', 'Учебный')], db_index=True, help_text='Вид отпуска', max_length=256, verbose_name='Вид отпуска'),
        ),
    ]
