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

# Ф-ия списка статей
def list_article(request):
    art_list = Article.objects.all().filter(date_of_delete=None, visibility=True)

    # Получение пременных из формы поиска
    search_query_name = request.GET.get('article_name', '')
    art_author = request.GET.get('article_author', '')

    dbl.log("fffff  "+ str(art_author))

    art_date_from = request.GET.get('article_date_from', '')
    art_date_to = request.GET.get('article_date_to', '')

    # НЕ РАБОТАЕТ
    # Здась планируется обработка запроса списка статей по автору ( когда на карточке статьи
    #  нажимают на автора, прогружается новый список статей с фильтром по автору )
    dbl.log("fffff")
    # auth_id = kwargs.get("author_id")
    # if auth_id:

    #     art_list = art_list.filter(author=auth_id, visibility=True, date_of_delete=None).order_by('-date_of_review')

            
    # # Получаем список тегов данной статьи
    # software_tag = Tag.objects.filter(softwares__id=software.id)


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

        

    # dbl.log(str(art_author))
    # if str(art_author).isdecimal():
    #     dbl.log("111")
    #     # art_author = User.get__name_surname(art_author)

    #     author = User.objects.get( id = art_author )

    #     art_author = str(author.name + " " + author.surname)
    #     dbl.log(str(art_author)+"fffff")

    # # else:
    # #     try:
    # #         pass
    # #     except ValueError:
    # #         pass

    # Фильтрация по дате начала отображения
    if art_date_from:
        # d = datetime.datetime.strptime("04.01.2020 12:13", '%d.%m.%Y %I:%M')
        date_from_for_db = datetime.datetime.strptime(art_date_from, '%d.%m.%Y')

        art_list = art_list.filter(date_of_review__gte=date_from_for_db)

    # Фильтрация по дате окончания отображения
    if art_date_to:
        
        date_to_for_db = datetime.datetime.strptime(art_date_to, '%d.%m.%Y')

        art_list = art_list.filter(date_of_review__lte=date_to_for_db)

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

    return render(request, 'article/articles.html', {'art_list':art_list, 'search_query_name':search_query_name, 'art_author':art_author, 'art_date_from':art_date_from, 'art_date_to':art_date_to})
