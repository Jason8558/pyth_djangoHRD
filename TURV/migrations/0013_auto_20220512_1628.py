# Generated by Django 3.1.7 on 2022-05-12 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0012_tabel_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabel',
            old_name='date',
            new_name='day',
        ),
    ]