# Generated by Django 3.0.5 on 2020-06-14 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20200520_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_addition',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название'),
        ),
    ]