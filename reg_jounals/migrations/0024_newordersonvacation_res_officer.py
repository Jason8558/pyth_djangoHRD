# Generated by Django 3.1.2 on 2021-01-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0023_auto_20210120_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='newordersonvacation',
            name='res_officer',
            field=models.CharField(blank=True, default='database', editable=False, help_text='Сотрудник, который создал приказ ', max_length=256, verbose_name='Ответственный сотрудник'),
        ),
    ]
