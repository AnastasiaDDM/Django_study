from django.db import models
from user.models import *
from .models import CustomUser
from django.conf import settings

class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete = models.PROTECT, verbose_name='Автор', null=True, blank=True)
    name = models.CharField('Название статьи', max_length = 200)
    text = models.TextField('Текст')
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)
    image = models.ImageField('Фото', blank=True, upload_to="article/")
    date_of_review = models.DateField('Дата публикации', blank=True, null=True)      
    date_of_delete = models.DateField('Дата удаления', blank=True, null=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
