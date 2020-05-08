# Generated by Django 3.0.5 on 2020-05-06 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='software.Software', verbose_name='ПО'),
        ),
        migrations.AlterField(
            model_name='classification_value',
            name='classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='software.Classification', verbose_name='Классификация'),
        ),
    ]
