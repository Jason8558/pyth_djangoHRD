# Generated by Django 4.1.1 on 2023-04-17 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0008_itemofresignation_letterofresignation_lor_itemofres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='addData',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Дополнительная информация'),
        ),
    ]
