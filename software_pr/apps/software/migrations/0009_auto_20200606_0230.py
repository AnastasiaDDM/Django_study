# Generated by Django 3.0.5 on 2020-06-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0008_software_name_small'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='description_small',
            field=models.TextField(max_length=150, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='software',
            name='name_small',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Мини-Наименование ПО'),
        ),
    ]
