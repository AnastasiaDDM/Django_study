# Generated by Django 3.0.5 on 2020-06-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200609_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='max_age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='expires',
            field=models.DateField(blank=True, null=True, verbose_name='Время действия кук'),
        ),
    ]