# Generated by Django 4.1.1 on 2022-10-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vac_shed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacantionsheduleitem',
            name='move_reason',
            field=models.TextField(default='', help_text='Введите основание переноса', verbose_name='Основание переноса'),
        ),
    ]