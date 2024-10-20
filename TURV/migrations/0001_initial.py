# Generated by Django 4.1.1 on 2022-10-12 22:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(db_index=True, max_length=256, verbose_name='Номер а\\м')),
                ('model', models.CharField(blank=True, max_length=256, null=True, verbose_name='Модель(необязательно) ')),
                ('unite_p', models.IntegerField(verbose_name='Процент доплаты')),
                ('used', models.BooleanField(default=1, verbose_name='Автомобиль используется')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
                'ordering': ['unite_p'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4, verbose_name='Наименование ')),
            ],
            options={
                'verbose_name': 'Категория',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256, verbose_name='Название подразделения')),
                ('onescode', models.CharField(blank=True, max_length=256, null=True, verbose_name='Код подразделения в 1С ')),
                ('notused', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(db_index=True, max_length=256, verbose_name='ФИО сотрудника')),
                ('sex', models.CharField(choices=[('М', 'М'), ('Ж', 'Ж')], db_index=True, default='М', max_length=1, verbose_name='Пол')),
                ('shift_personnel', models.BooleanField(default=False, verbose_name='Сменный персонал')),
                ('fired', models.BooleanField(default=False, verbose_name='Сотрудник уволен')),
                ('stand_worktime', models.FloatField(default=0, verbose_name='Норма часов')),
                ('level', models.CharField(max_length=256, verbose_name='Разряд/категория')),
                ('positionOfPayment', models.CharField(max_length=3, verbose_name='Ступень оплаты')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.department', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['fullname'],
            },
        ),
        migrations.CreateModel(
            name='FeedBackTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Виды сообщений от пользователей',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(db_index=True, verbose_name='Период')),
                ('value_m', models.FloatField(default=0, verbose_name='Значение_мужчины')),
                ('value_w', models.FloatField(default=0, verbose_name='Значение_женщины')),
            ],
            options={
                'verbose_name': 'Норма времени',
                'verbose_name_plural': 'Нормы врмени',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256, verbose_name='Название должности')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(db_index=True, max_length=4, verbose_name='Год')),
                ('month', models.CharField(db_index=True, max_length=256, verbose_name='Месяц')),
                ('day', models.CharField(blank=True, db_index=True, default='0', max_length=256, null=True, verbose_name='Число')),
                ('del_check', models.BooleanField(blank=True, default=False, verbose_name='Пометка удаления')),
                ('sup_check', models.BooleanField(blank=True, default=False, verbose_name='Проверен СУП')),
                ('paper_check', models.BooleanField(default=False, verbose_name='Сдан в бумажном виде')),
                ('unloaded', models.BooleanField(blank=True, default=False, verbose_name='Загружен в 1С')),
                ('comm', models.CharField(blank=True, default='', max_length=256, verbose_name='Комментарий (НЕОБЯЗАТЕЛЬНО)')),
                ('iscorr', models.BooleanField(default=False)),
                ('res_officer', models.CharField(blank=True, editable=False, help_text='Отвественный за составление табеля', max_length=256, verbose_name='Табельщик')),
                ('corr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TURV.tabel', verbose_name='Корректировка к ')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.department', verbose_name=' ')),
            ],
            options={
                'verbose_name': 'Табель',
                'verbose_name_plural': 'Табели',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='TabelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Вид табеля ')),
            ],
            options={
                'verbose_name': 'Вид табеля',
                'verbose_name_plural': 'Виды табеля',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TabelItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(db_index=True, max_length=256, verbose_name='Год')),
                ('month', models.CharField(db_index=True, max_length=256, verbose_name='Месяц')),
                ('toxic_p', models.IntegerField(blank=True, default=0, null=True, verbose_name='Процент доплаты за вредность')),
                ('type_time1', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени1')),
                ('type_time2', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени2')),
                ('type_time3', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени3')),
                ('type_time4', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени4')),
                ('type_time5', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени5')),
                ('type_time6', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени6')),
                ('type_time7', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени7')),
                ('type_time8', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени8')),
                ('type_time9', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени9')),
                ('type_time10', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени10')),
                ('type_time11', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени11')),
                ('type_time12', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени12')),
                ('type_time13', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени13')),
                ('type_time14', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени14')),
                ('type_time15', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени15')),
                ('type_time16', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени16')),
                ('type_time17', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени17')),
                ('type_time18', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени18')),
                ('type_time19', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени19')),
                ('type_time20', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени20')),
                ('type_time21', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени21')),
                ('type_time22', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени22')),
                ('type_time23', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени23')),
                ('type_time24', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени24')),
                ('type_time25', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени25')),
                ('type_time26', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени26')),
                ('type_time27', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени27')),
                ('type_time28', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени28')),
                ('type_time29', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени29')),
                ('type_time30', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени30')),
                ('type_time31', models.CharField(blank=True, max_length=4, null=True, verbose_name='Вид времени31')),
                ('hours1', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы1')),
                ('hours2', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы2')),
                ('hours3', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы3')),
                ('hours4', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы4')),
                ('hours5', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы5')),
                ('hours6', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы6')),
                ('hours7', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы7')),
                ('hours8', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы8')),
                ('hours9', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы9')),
                ('hours10', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы10')),
                ('hours11', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы11')),
                ('hours12', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы12')),
                ('hours13', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы13')),
                ('hours14', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы14')),
                ('hours15', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы15')),
                ('hours16', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы16')),
                ('hours17', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы17')),
                ('hours18', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы18')),
                ('hours19', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы19')),
                ('hours20', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы20')),
                ('hours21', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы21')),
                ('hours22', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы22')),
                ('hours23', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы23')),
                ('hours24', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы24')),
                ('hours25', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы25')),
                ('hours26', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы26')),
                ('hours27', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы27')),
                ('hours28', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы28')),
                ('hours29', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы29')),
                ('hours30', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы30')),
                ('hours31', models.CharField(blank=True, max_length=10, null=True, verbose_name='Часы31')),
                ('sHours1', models.FloatField(blank=True, help_text='Явки', null=True, verbose_name='Явки (Я)')),
                ('sHours2', models.FloatField(blank=True, null=True, verbose_name='Ночные (Н)')),
                ('sHours3', models.IntegerField(blank=True, null=True, verbose_name='Работа в выходные и празд. (РВ)')),
                ('sHours4', models.FloatField(blank=True, null=True, verbose_name='Сверхурочные (С)')),
                ('sHours5', models.IntegerField(blank=True, null=True, verbose_name='Вахтовый метод (ВМ)')),
                ('sHours6', models.IntegerField(blank=True, null=True, verbose_name='Служебная командировка (К)')),
                ('sHours7', models.IntegerField(blank=True, null=True, verbose_name='Повыш. квалификации с отрывом от работы (ПК)')),
                ('sHours8', models.IntegerField(blank=True, null=True, verbose_name='Повыш. квалификации с отрывом от рб. в другой мес-ти (ПМ)')),
                ('sHours9', models.IntegerField(blank=True, null=True, verbose_name='Основной оплачиваемый отпуск (ОТ)')),
                ('sHours10', models.IntegerField(blank=True, null=True, verbose_name='Дополнительный оплачиваемый отпуск (ОД)')),
                ('sHours11', models.IntegerField(blank=True, null=True, verbose_name='Учебный отпуск (У)')),
                ('sHours12', models.IntegerField(blank=True, null=True, verbose_name='Сокращенная продолжительность для обучающихся без отрыва (УВ)')),
                ('sHours13', models.IntegerField(blank=True, null=True, verbose_name='Неоплачиваемый учебный отпуск (УД)')),
                ('sHours14', models.IntegerField(blank=True, null=True, verbose_name='Отпуск по беременности и родам (Р)')),
                ('sHours15', models.IntegerField(blank=True, null=True, verbose_name='Отпуск по уходу за ребенком до 3-х лет (ОЖ)')),
                ('sHours16', models.IntegerField(blank=True, null=True, verbose_name='Отпуск без сохр. зп по разрешению работодателя (ДО)')),
                ('sHours17', models.IntegerField(blank=True, null=True, verbose_name='Временная нетрудоспособность (Б)')),
                ('sHours18', models.IntegerField(blank=True, null=True, verbose_name='Неоплачиваемый больничный (Т)')),
                ('sHours19', models.IntegerField(blank=True, null=True, verbose_name='Сокращенная продолжительность рабочего времени (ЛЧ)')),
                ('sHours20', models.IntegerField(blank=True, null=True, verbose_name='Время вынужденного прогула в случае признания увольнения незаконным (ПВ)')),
                ('sHours21', models.IntegerField(blank=True, null=True, verbose_name='Невыходы на время исполнения гос. ил общ. обязанностей (Г)')),
                ('sHours22', models.IntegerField(blank=True, null=True, verbose_name='Прогулы (ПР)')),
                ('sHours23', models.IntegerField(blank=True, null=True, verbose_name='Работа в режиме неполного рабочего времени (НС)')),
                ('sHours24', models.IntegerField(blank=True, null=True, verbose_name='Выходные (В)')),
                ('sHours25', models.IntegerField(blank=True, null=True, verbose_name='Дополнительные выходные оплачиваемые (ОВ)')),
                ('sHours26', models.IntegerField(blank=True, null=True, verbose_name='Дополнительные выходные неоплачиваемые (НВ)')),
                ('sHours27', models.IntegerField(blank=True, null=True, verbose_name='Забастовка (ЗБ)')),
                ('sHours28', models.IntegerField(blank=True, null=True, verbose_name='Неявки по невыясненным причинам (НН)')),
                ('sHours29', models.IntegerField(blank=True, null=True, verbose_name='Время простоя по вине работодателя (РП)')),
                ('sHours30', models.IntegerField(blank=True, null=True, verbose_name='Время простоя по причинам, не зависищим от работника и работодателя (НП)')),
                ('sHours31', models.IntegerField(blank=True, null=True, verbose_name='Время простоя по вине работника (ВП)')),
                ('sHours32', models.IntegerField(blank=True, null=True, verbose_name='Оплачиваемое отстранение от работы (НО)')),
                ('sHours33', models.IntegerField(blank=True, null=True, verbose_name='Неоплачиваемое отстранение от работы (НБ)')),
                ('sHours34', models.IntegerField(blank=True, null=True, verbose_name='Остановка работы про причине невыплаты ЗП (НЗ)')),
                ('sHours35', models.IntegerField(blank=True, null=True, verbose_name='Совмещение')),
                ('sHours36', models.IntegerField(blank=True, null=True, verbose_name='Местная командировка')),
                ('sHours37', models.IntegerField(blank=True, null=True, verbose_name='Пенсионный')),
                ('sHours38', models.IntegerField(blank=True, null=True, verbose_name='Нерабочие оплачиваемые дни')),
                ('sHours39', models.IntegerField(blank=True, null=True, verbose_name='Отсутствие по мобилизации')),
                ('w_days', models.IntegerField(blank=True, default=0, null=True, verbose_name='Дней отработано')),
                ('w_hours', models.FloatField(blank=True, default=0, null=True, verbose_name='Часов отработано')),
                ('v_days', models.IntegerField(blank=True, default=0, null=True, verbose_name='Дней неявок')),
                ('v_hours', models.FloatField(blank=True, default=0, null=True, verbose_name='Часов неявок')),
                ('auto', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='TURV.automobile', verbose_name='а/м')),
                ('bound_tabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.tabel', verbose_name='Св. табель')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.employers', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Сотрудник в табеле',
                'verbose_name_plural': 'Сотрудники в табелях',
                'ordering': ['-year'],
            },
        ),
        migrations.AddField(
            model_name='tabel',
            name='type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='TURV.tabeltype', verbose_name='Вид '),
        ),
        migrations.CreateModel(
            name='InfoMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст сообщения: ')),
                ('alldeps', models.BooleanField(default=True, verbose_name='Для всех')),
                ('active', models.BooleanField(default=True, verbose_name='Сообщение активно')),
                ('dfrom', models.DateField(blank=True, null=True, verbose_name='Дата начала показа: ')),
                ('dto', models.DateField(blank=True, null=True, verbose_name='Дата окончания показа: ')),
                ('always', models.BooleanField(default=True, verbose_name='Показывать постоянно')),
                ('viewin', models.CharField(choices=[('1', 'Главное окно'), ('2', 'Окно табеля'), ('3', 'Окно редактирования табеля')], default='1', max_length=100)),
                ('alltypes', models.BooleanField(default=True, verbose_name='Для всех видов табеля')),
                ('mestype', models.CharField(choices=[('1', 'Обычное'), ('2', 'О переносе отпуска')], default='1', max_length=100)),
                ('important', models.BooleanField(default=False, verbose_name='Особо важное')),
                ('deps', models.ManyToManyField(blank=True, null=True, to='TURV.department', verbose_name='Подразделения, для которых предназначена информация: ')),
                ('intypes', models.ManyToManyField(default='1', to='TURV.tabeltype', verbose_name='Отображать в табелях: ')),
            ],
            options={
                'verbose_name': 'Сообщение пользователям',
                'verbose_name_plural': 'Система оповещения пользователей',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('about', models.CharField(max_length=100, verbose_name='Тема')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('inwork', models.BooleanField(default=False, verbose_name='Принято в работу')),
                ('readed', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Ответ на сообщение')),
                ('answer_readed', models.BooleanField(default=False, verbose_name='Ответ прочитан')),
                ('mes_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.feedbacktypes', verbose_name='Вид сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение от пользователя',
                'verbose_name_plural': 'Сообщения пользователей',
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='employers',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.position', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='department',
            name='conftype',
            field=models.ManyToManyField(to='TURV.tabeltype', verbose_name='Виды табелей для подразделения: '),
        ),
        migrations.AddField(
            model_name='department',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Табельщик'),
        ),
    ]
