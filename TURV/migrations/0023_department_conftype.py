# Generated by Django 3.1.7 on 2022-05-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0022_auto_20220523_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='conftype',
            field=models.ManyToManyField(to='TURV.TabelType', verbose_name='Виды табелей для подразделения: '),
        ),
    ]