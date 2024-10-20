# Generated by Django 4.1.1 on 2023-03-29 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0016_tabel_half_month_check'),
        ('shift_shed', '0007_shiftsheditem_norma'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResEmloyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=250, verbose_name='Полная должность')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.department', verbose_name='Подразделение')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.employers', verbose_name='ФИО руководителя')),
            ],
            options={
                'verbose_name': 'Согласующие руководители',
                'ordering': ['emp'],
            },
        ),
    ]
