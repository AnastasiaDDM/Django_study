# Generated by Django 3.0.5 on 2020-05-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст')),
                ('visibility', models.BooleanField(db_index=True, default=True, verbose_name='Видимость на сайте')),
                ('image', models.ImageField(blank=True, upload_to='article/', verbose_name='Фото')),
                ('date_of_review', models.DateField(blank=True, null=True, verbose_name='Дата публикации')),
                ('date_of_delete', models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата удаления')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
