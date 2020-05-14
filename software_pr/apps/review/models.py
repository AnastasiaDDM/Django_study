from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User
from software.models import Software

class Review(models.Model):

    company = 'com'
    order = 'ord'
    software = 'sof'

    KIND_REVIEW = (
        (company, 'Компания'),
        (order, 'Заказ'),
        (software, 'ПО'),
    )

    kind = models.CharField(max_length=3, choices=KIND_REVIEW, default=company, db_index=True)
    client = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name='Клиент', null=True, blank=True)
    name = models.CharField('Имя', max_length = 100, null=True, blank=True)
    email_phone = models.CharField('Телефон', max_length = 60, null=True, blank=True)
    content = models.TextField('Отзыв', null=True, blank=True)
    comment = models.TextField('Комментарий к отзыву', null=True, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True, blank=True)
    software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО', null=True, blank=True)
    star = models.IntegerField('Оценка',  default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_of_delete = models.DateField('Дата удаления', blank=True, db_index=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
