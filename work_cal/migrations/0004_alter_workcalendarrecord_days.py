# Generated by Django 4.1.1 on 2023-05-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_cal', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workcalendarrecord',
            name='days',
            field=models.CharField(blank=True, max_length=256, verbose_name='Дни'),
        ),
    ]