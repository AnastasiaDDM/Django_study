from django.db import models
from django.core.validators import MinValueValidator
from user.models import User

class Feedback(models.Model):
    name = models.CharField('Имя', max_length = 100, null=True, blank=True)
    client = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name='Клиент', null=True, blank=True)
    phone = models.CharField('Телефон', max_length = 20)
    comment = models.TextField('Комментарий', null=True, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Заказ звонка'
        verbose_name_plural = 'Заказ звонка'


