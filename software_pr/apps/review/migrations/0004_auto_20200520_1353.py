# Generated by Django 3.0.5 on 2020-05-20 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_addition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_addition',
            name='date_of_delete',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата удаления'),
        ),
    ]
