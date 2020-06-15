from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
import request
from article.models import *
from .models import Article
from .models import CustomUser
from django.db import models
from django.db.models import Q
from django.core.paginator import *
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpRequest
import dbl
import re

# Ф-ия списка статей
def list_article(request):
    art_list = Article.objects.all().filter(date_of_delete=None, visibility=True)

    list_tags = []

    # Получение пременных из формы поиска
    search_query_name = request.GET.get('article_name', '')
    art_author = request.GET.get('article_author', '')
    art_date_from = request.GET.get('article_date_from', '')
    art_date_to = request.GET.get('article_date_to', '')
    search_query_tags = request.GET.get('article_tags', '')

    # Фильтрация по наименовании статьи
    if search_query_name:
        art_list = art_list.filter(name__icontains=search_query_name, visibility=True, date_of_delete=None)

    # Фильтрация по автору
    if art_author:

        # Введен id 
        if str(art_author).isdigit():

            art_list = art_list.filter(author__id=int(art_author), date_of_delete=None)

            try:
                author = CustomUser.objects.get( id = art_author )
                art_author = str(author.name + " " + author.surname)
            except :
                pass

        else :

            art_list = art_list.filter((Q(author__name__icontains=art_author) | Q(author__surname__icontains=art_author) | Q(author__patronymic__icontains=art_author)), date_of_delete=None)


    # Фильтрация по дате начала отображения
    if art_date_from:
        # d = datetime.datetime.strptime("04.01.2020 12:13", '%d.%m.%Y %I:%M')
        date_from_for_db = datetime.datetime.strptime(art_date_from, '%d.%m.%Y')

        art_list = art_list.filter(date_of_review__gte=date_from_for_db)

    # Фильтрация по дате окончания отображения
    if art_date_to:
        
        date_to_for_db = datetime.datetime.strptime(art_date_to, '%d.%m.%Y')

        art_list = art_list.filter(date_of_review__lte=date_to_for_db)

    # Фильтрация по списку тегов статей
    if search_query_tags:

        # Сплит строки запроса
        list_tags = re.split(r'[ ,]+', search_query_tags)

        # Фильтрация статей по списку тегов
        art_list = Article.get_articles_by_tags(art_list, list_tags)

    art_list = art_list.order_by('-date_of_review')

    # НЕ РАБОТАЕТ
    # Поля выбора отображения на странице (мгновенное изменение) пока не работает(
    count = int(request.GET.get('count', '10000'))
    dbl.log(str(count)+"fffff")

    paginator = Paginator( art_list, count )

    try:
        page = int(request.GET.get('page', '1'))

    except:
        page = 1
    
    try:
        art_list = paginator.page(page)
        dbl.log(str(page))
        dbl.log("пагинация")
    except(EmptyPage, InvalidPage):
        art_list = paginator.page(paginator.num_pages) 
        dbl.log("!!пагинация")

    return render(request, 'article/articles.html', {'art_list':art_list, 'search_query_name':search_query_name, 'art_author':art_author,
    'list_tags':list_tags, 'art_date_from':art_date_from, 'art_date_to':art_date_to})
