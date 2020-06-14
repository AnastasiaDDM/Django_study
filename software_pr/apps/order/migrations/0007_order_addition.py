# Generated by Django 3.0.5 on 2020-06-12 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200612_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Addition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('kind', models.BooleanField(default=True, verbose_name='Тип (true - картинка)')),
                ('size', models.BooleanField(default=True, verbose_name='Тип (true - большая картинка)')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='order/', verbose_name='Фото')),
                ('file', models.FileField(blank=True, null=True, upload_to='file_order/', verbose_name='Ссылка на файл')),
                ('is_main', models.BooleanField(default=False, verbose_name='Тип (true - главная)')),
                ('date_of_delete', models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата удаления')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.Order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Приложение',
                'verbose_name_plural': 'Приложения',
            },
        ),
    ]
