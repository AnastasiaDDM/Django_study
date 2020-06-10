#editor.detectIndentation#
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.db import models
from software.models import *
from django.db.models import Q
from django.core.paginator import *
import dbl
import re
from user.models import CustomUser
from user.forms import Register_by_email_phone_Form
import util.views
import json
from django.template.loader import render_to_string
from discussion.views import render_discussion_comment


# Ф-ия составления списка ПО
def catalog(request):
    soft_list = Software.objects.all().filter(date_of_delete=None, visibility=True)

    # Получение пременных из формы поиска
    search_query_name = request.GET.get('soft_name', '')
    soft_price = request.GET.get('soft_price', '')
    soft_pricefrom = request.GET.get('soft_pricefrom', '')
    soft_priceto = request.GET.get('soft_priceto', '')
    modification = request.GET.get('modification', '')

    # Словарь для фильтра классификаций
    classification_dict = {}

    # Перебор всех прищедших аргументов
    for req in request.GET.items():

        # Проверка валидности значения имени (классификации)
        if re.match(r'classification_(\d+)_value_(\d+)', str(req[0])):

            # Проверка значения поля формы поиска
            if str(req[1]) !="" and str(req[1]).isdigit():

                # Добавление значения в словарь
                classification_dict[str(req[0])] = str(req[1])

    #  Перменная составления запроса с фильтрами по классификациям
    cond = Q()

    # перебор словаря классификаций
    for cl_val in classification_dict.values():

        # Добавление условия фильтрации
        cond |=Q(classification_value=int(cl_val))

    # Фильтрация списка всех ПО по выбранным классификациям
    soft_list = soft_list.filter(cond)

    # Исключение повторений ПО
    soft_list = soft_list.order_by('id').distinct()



    # Фильтрация по цене (бесплатные ПО)
    if soft_price =="soft_price_free":
        soft_list = soft_list.filter(price=0)

    # Фильтрация по цене (платные ПО)
    if soft_price =="soft_price_paid":
        soft_list = soft_list.exclude(price=0)

    # Фильтрация по начальной цене
    if soft_pricefrom:
        soft_list = soft_list.filter(price__gte=soft_pricefrom)

    # Фильтрация по конечной цене
    if soft_priceto:
        soft_list = soft_list.filter(price__lte=soft_priceto)

    # Фильтрация по наименованию ПО
    if search_query_name:
        soft_list = soft_list.filter(name__icontains=search_query_name)


    # Фильтрация по полю доработки
    if modification:
        soft_list = soft_list.filter(modification=True)


    count = request.GET.get('count', '10')
    if count == "":
        count = 10
    count = int(count)

    paginator = Paginator( soft_list, count )

    try:
        page = int(request.GET.get('page', '1'))

    except:
        page = 1
    
    try:
        soft_list = paginator.page(page)
        # dbl.log(str(page))
        # dbl.log("пагинация")
    except(EmptyPage, InvalidPage):
        soft_list = paginator.page(paginator.num_pages) 
        # dbl.log("!!пагинация")

    # Хэш классификаций ПО
    tags_dict = {}
    photo_dict = {}

    for soft in soft_list:

        soft_tags_list = soft.get_tags()

        soft_photo = soft.get_main_photo()

        # Добавляем ключ и значение в словарь
        tags_dict[soft.id] = soft_tags_list

        if soft_photo is not None:
            # dbl.log("колво "+str(count(soft_photo)))
            # if count(soft_photo) >1:

            # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
            for s in soft_photo:
                photo_dict[soft.id] = s

    # Получение текущего пользователя 
    user = CustomUser.get_user(request)

    # Получение списка всех видов ПО
    classifications = Classification.objects.all().filter(date_of_delete=None, visibility=True).order_by('id')

    response = render(request, 'soft/catalog.html', {'soft_list':soft_list, 'photo_dict':photo_dict, 'count':count, 'modification':modification, 
    'search_query_name':search_query_name, 'soft_price':soft_price, 'soft_pricefrom':soft_pricefrom, 
    'soft_priceto':soft_priceto, 'tags_dict':tags_dict, 'classifications':classifications, 
    'classification_dict':classification_dict, 'user':user})
    return response


# Страница одного ПО
def software_page(request, id):

    # Объявление начальных значений переменных
    # Хэш классификаций ПО
    classif = {}
    software = Software()
    software_img = Q()
    main_photo = Q()
    software_tag = Q()
    list_descr = []
    similar_block = ""
    similar_tags_block = ""
    discussion_comment_block = ""

    try:
        software = Software.objects.get( id = id )

        #  Получение главного фото
        main_photo_query = software.get_main_photo()
        dbl.log("сойт 2  " + str(main_photo_query))


        # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
        for photo in main_photo_query:
            main_photo = photo
        
        dbl.log("сойт 3  " + str(main_photo))

        # Получаем список приложений данного ПО (ФАЙЛЫ, ФОТОГРАФИИ)
        software_img = software.get_addition()

        dbl.log("сойт 4  " + str(software_img))

        # Исключения главного фото (main_photo) из списка фото
        if software_img:
            software_img = software_img.exclude(pk=main_photo.id)

        # Получаем список тегов данного ПО
        software_tag = software.get_tags()

        #  Для разрыва текста (скрытого и открытого)
        # Сплит строки по '\n' по первому вхождению - получаем массив элементов одной переменной
        list_descr = software.description.split('\n', 1)

        # Получаем список классификаций данного ПО
        classif = software.get_classifications()

        # ar = software.get_area()

        # Второстепенные объекты - похожие ПО
        similar_block = render_similars(software)
        similar_tags_block = render_similars_tags(software)
        discussion_comment_block = render_discussion_comment(software, request, limit=5)

        # Получение текущего пользователя 
        user = CustomUser.get_user(request)
        
        return render(request, 'soft/software.html', {'software':software, 'software_img':software_img, 'main_photo':main_photo, 'classif':classif,
        'list_descr':list_descr, 'software_tag':software_tag, 'similar_block':similar_block, 'similar_tags_block':similar_tags_block,
        'discussion_comment_block':discussion_comment_block, 'user':user})


    # except:
    #     raise Http404("ПО не найдено")

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    # return render(request, 'soft/software.html', {'software':software, 'software_img':software_img, 'main_photo':main_photo, 'classif':classif,
    # 'list_descr':list_descr, 'software_tag':software_tag, 'similar_block':similar_block, 'similar_tags_block':similar_tags_block,
    # 'discussion_comment_block':discussion_comment_block})

    raise Http404("ПО не найдено")



# Ф-ия добавления избранного
def add_favourite(request, software_id):

    try:
        # Объявление начальных значений
        user = None
        cookie = {}

        # Получение текущего пользователя 
        user, cookie = CustomUser.get_user_or_create(request)

        if user:

            software = Software.objects.get( id = int(software_id) )

            data = { 'status': 'success' }

            fav = software.is_favourite(user)

            if fav:
                
                fav.delete()

                data['result'] = False  
                
            else:
                Favourite.objects.create(client=user, software=software)

                data['result'] = True

            response = HttpResponse(json.dumps(data), content_type='application/json')
            response = util.views.wrap_cookie(response, cookie)
            return response

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    return redirect('software:catalog')


# Ф-ия отображения страницы покупки
def software_buy(request, software_id):

    form = Register_by_email_phone_Form()

    try:
        # Объявление начальных значений
        user = None
        cookie = {}

        # Получение текущего пользователя 
        user, cookie = CustomUser.get_user_or_create(request)

        if user:

            software = Software.objects.get( id = int(software_id) )

            response = render(request, 'soft/buy.html', {'software':software, 'user':user})
            response = util.views.wrap_cookie(response, cookie)
            return response

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    return redirect('software:catalog')


# Ф-ия отображения страницы покупки
def software_download(request, software_id):

    form = Register_by_email_phone_Form()

    try:
        # Объявление начальных значений
        user = None
        cookie = {}

        # Получение текущего пользователя 
        user, cookie = CustomUser.get_user_or_create(request)

        if user:

            software = Software.objects.get( id = int(software_id) )

            response = render(request, 'soft/download.html', {'software':software, 'user':user})
            response = util.views.wrap_cookie(response, cookie)
            return response

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    return redirect('software:catalog')



# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ

# Ф-ия создания кода html для похожих ПО
def render_similars(software):

    # Получение списка похожих ПО
    similar_list = software.get_similars()

    # Хэш фотографий ПО
    photo_dict = {}
    result =''

    for soft in similar_list:

        soft_photo = soft.get_main_photo()

        # Добавляем ключ и значение в словарь
        if soft_photo is not None:
            for s in soft_photo:
                photo_dict[soft.id] = s

    result = render_to_string('common/pattern_similars.html', {'similar_list':similar_list, 'photo_dict':photo_dict})
    return result


# Ф-ия создания кода html для облака тегов к ПО
def render_similars_tags(software):

    # Получение списка тегов похожих ПО
    similar_tags_list = software.get_similars_tags()
    result =''

    result = render_to_string('common/pattern_similars_tags.html', {'similar_tags_list':similar_tags_list})
    return result