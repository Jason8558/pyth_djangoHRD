# Generated by Django 3.1.7 on 2022-05-22 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0021_department_notused'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomessages',
            name='alltypes',
            field=models.BooleanField(default=True, verbose_name='Для всех видов табеля'),
        ),
        migrations.AlterField(
            model_name='infomessages',
            name='always',
            field=models.BooleanField(default=True, verbose_name='Показывать постоянно'),
        ),
    ]