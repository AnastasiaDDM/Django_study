# Generated by Django 3.0.5 on 2020-05-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200523_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='Админ'),
        ),
    ]
