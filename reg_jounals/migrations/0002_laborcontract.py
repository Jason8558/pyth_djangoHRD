# Generated by Django 3.1.2 on 2020-12-23 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaborContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_number', models.CharField(db_index=True, help_text='Введите номер договора', max_length=5, verbose_name='Номер договора')),
                ('lc_date', models.DateField(db_index=True, help_text='Введите дату договора', verbose_name='Дата договора')),
                ('lc_emloyer', models.CharField(db_index=True, help_text='Введите ФИО принимаемого сотрудника', max_length=256, verbose_name='ФИО принимаемого сотрудника')),
                ('lc_dateOfInv', models.DateField(db_index=True, help_text='Введите дату приема на работу', verbose_name='Дата приема на работу')),
                ('lc_workCond', models.CharField(db_index=True, help_text='Введите условие работы', max_length=256, verbose_name='Условие работы')),
                ('lc_res_officer', models.CharField(blank=True, editable=False, help_text='Сотрудник, который внес документ в систему ', max_length=256, verbose_name='Ответственный сотрудник')),
                ('lc_dep', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='reg_jounals.departments', verbose_name='Подразделение ')),
            ],
            options={
                'verbose_name': 'Трудовой договор',
                'verbose_name_plural': 'Трудовые договоры',
                'ordering': ['lc_number'],
            },
        ),
    ]
