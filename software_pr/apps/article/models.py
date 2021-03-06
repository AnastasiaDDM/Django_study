from django.db import models
from user.models import CustomUser
from django.conf import settings
import software.models as software_models

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


    # Ф-ия получения списка тегов 
    def get_tags(self):

        # Получаем список тегов данного ПО
        article_tag = software_models.Tag.objects.filter(articles__id=self.id, visibility=True, date_of_delete=None)
        return article_tag

    @staticmethod
    # Ф-ия получения списка ПО по тегам
    def get_articles_by_tags(article_list, list_tags):
        return article_list.filter(tag__name__in=list_tags).distinct()