# Generated by Django 3.0.5 on 2020-06-18 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_chat_chat_addition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='chat_order', to='order.Order', verbose_name='Заказ'),
        ),
    ]
