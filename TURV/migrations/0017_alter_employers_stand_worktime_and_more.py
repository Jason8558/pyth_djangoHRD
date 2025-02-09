# Generated by Django 4.1.1 on 2024-07-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0016_tabel_half_month_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='stand_worktime',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Норма часов'),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='value_m',
            field=models.FloatField(default=0, verbose_name='Норма времени для мужчин'),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='value_w',
            field=models.FloatField(default=0, verbose_name='Норма времени для женщин'),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='year',
            field=models.DateField(db_index=True, verbose_name='Период (первое число года)'),
        ),
    ]
