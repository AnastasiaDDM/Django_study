# Generated by Django 3.0.5 on 2020-05-13 16:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('software', '0008_classification_value_softwares'),
        ('user', '0003_auto_20200507_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('com', 'Компания'), ('ord', 'Заказ'), ('sof', 'ПО')], db_index=True, default='com', max_length=3)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('email_phone', models.CharField(blank=True, max_length=60, null=True, verbose_name='Телефон')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Отзыв')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к отзыву')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('star', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('date_of_delete', models.DateField(blank=True, db_index=True, verbose_name='Дата удаления')),
                ('visibility', models.BooleanField(db_index=True, default=True, verbose_name='Видимость на сайте')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.User', verbose_name='Клиент')),
                ('software', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='software.Software', verbose_name='ПО')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
