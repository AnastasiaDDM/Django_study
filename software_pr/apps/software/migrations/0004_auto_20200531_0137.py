# Generated by Django 3.0.5 on 2020-05-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_auto_20200526_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification',
            name='date_of_delete',
            field=models.DateField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_of_delete',
            field=models.DateField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
    ]