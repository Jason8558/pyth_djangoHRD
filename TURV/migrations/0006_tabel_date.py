# Generated by Django 3.1.7 on 2022-05-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0005_auto_20220421_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel',
            name='date',
            field=models.DateField(blank=True, db_index=True, default='2000-01-01', verbose_name='Число'),
        ),
    ]