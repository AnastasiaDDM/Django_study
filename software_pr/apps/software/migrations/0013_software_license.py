# Generated by Django 3.0.5 on 2020-06-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0012_software_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='license',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания лицензии'),
        ),
    ]
