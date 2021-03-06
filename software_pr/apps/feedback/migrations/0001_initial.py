# Generated by Django 3.0.5 on 2020-05-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заказ звонка',
                'verbose_name_plural': 'Заказ звонка',
            },
        ),
    ]
