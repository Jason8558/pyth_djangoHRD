# Generated by Django 3.1.2 on 2021-01-31 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0028_auto_20210125_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laborcontract',
            name='lc_number',
            field=models.CharField(db_index=True, help_text='Введите номер договора', max_length=256, verbose_name='Номер договора'),
        ),
    ]
