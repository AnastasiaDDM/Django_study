# Generated by Django 3.0.5 on 2020-06-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Наименование заказа'),
        ),
    ]
