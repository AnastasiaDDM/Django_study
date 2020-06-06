from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import CustomUser
from software.models import Software

class Discussion(models.Model):

    client = models.ForeignKey(CustomUser, on_delete = models.PROTECT, verbose_name='Клиент', null=True, blank=True)
    name = models.CharField('Имя', max_length = 100, null=True, blank=True)
    email_phone = models.CharField('Телефон', max_length = 60, null=True, blank=True)
    content = models.TextField('Обсуждение')
    date = models.DateTimeField('Дата', auto_now_add=True, blank=True)
    software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО', null=True, blank=True)
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'

    # Ф-ия получения списка приложений
    # def get_addition(self):

    #     # Получаем список приложений данного отзыва
    #     list_img = Review_Addition.objects.filter(review__id = self.id, date_of_delete=None)
    #     return list_img


class Comment(models.Model):

    discussion = models.ForeignKey(Discussion, on_delete = models.PROTECT, verbose_name='Обсуждение', related_name='discussion')
    client = models.ForeignKey(CustomUser, on_delete = models.PROTECT, verbose_name='Клиент', null=True, blank=True, related_name='comment_client')
    name = models.CharField('Имя', max_length = 100, null=True, blank=True)
    email_phone = models.CharField('Телефон', max_length = 60, null=True, blank=True)
    content = models.TextField('Обсуждение')
    date = models.DateTimeField('Дата', auto_now_add=True, blank=True)
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
