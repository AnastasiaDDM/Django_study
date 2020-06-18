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
import util.views
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
    sort_param = request.GET.get('sort')
    if sort_param is None:
        sort_param = ""
    count = request.GET.get('count', '10')
    if count == "":
        count = 10
    count = int(count)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

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

    # Сортировка, показать по, перейти на страницу
    art_list = util.views.sort_show_by(art_list, sort_param, count, page )

    return render(request, 'article/articles.html', {'art_list':art_list, 'search_query_name':search_query_name, 'art_author':art_author,
    'list_tags':list_tags, 'art_date_from':art_date_from, 'art_date_to':art_date_to})




# Страница одного ПО
def article_page(request, id):

    # Объявление начальных значений переменных
    # Хэш классификаций ПО
    # classif = {}
    article = Article()
    # software_img = Q()
    # main_photo = Q()
    # software_tag = Q()
    # list_descr = []
    # similar_block = ""
    # similar_tags_block = ""
    # discussion_comment_block = ""

    # Строка фильтра для хлебных крошек
    # str_filter_for_breadcrumb = ""

    try:
        article = Article.objects.get( id = id )

        #  Получение главного фото
        # main_photo_query = software.get_main_photo()
        # dbl.log("сойт 2  " + str(main_photo_query))


        # # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
        # for photo in main_photo_query:
        #     main_photo = photo
        
        # dbl.log("сойт 3  " + str(main_photo))

        # # Получаем список приложений данного ПО (ФАЙЛЫ, ФОТОГРАФИИ)
        # software_img = software.get_addition()

        # dbl.log("сойт 4  " + str(software_img))

        # # Исключения главного фото (main_photo) из списка фото
        # if software_img:
        #     software_img = software_img.exclude(pk=main_photo.id)

        # # Получаем список тегов данного ПО
        # software_tag = software.get_tags()

        # #  Для разрыва текста (скрытого и открытого)
        # # Сплит строки по '\n' по первому вхождению - получаем массив элементов одной переменной
        # list_descr = software.description.split('\n', 1)

        # # Получаем список классификаций данного ПО
        # classif, str_filter_for_breadcrumb = software.get_classifications()

        # # Второстепенные объекты - похожие ПО
        # similar_block = render_similars(software, id_widget="same_software")
        # similar_tags_block = render_similars_tags(software)
        # discussion_comment_block = render_discussion_comment(software, request, limit=5)

        # Получение текущего пользователя 
        user = CustomUser.get_user(request)
        
        return render(request, 'article/article.html', {'article':article, 'user':user})


    # except:
    #     raise Http404("ПО не найдено")

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    # return render(request, 'soft/software.html', {'software':software, 'software_img':software_img, 'main_photo':main_photo, 'classif':classif,
    # 'list_descr':list_descr, 'software_tag':software_tag, 'similar_block':similar_block, 'similar_tags_block':similar_tags_block,
    # 'discussion_comment_block':discussion_comment_block})

    raise Http404("ПО не найдено")
