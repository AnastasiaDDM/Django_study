#editor.detectIndentation#
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.db import models
from software.models import *
from django.db.models import Q
from django.core.paginator import *
import dbl
import re
from user.models import CustomUser



    

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
            for s in soft_photo:
                photo_dict[soft.id] = s


    # Получение списка всех видов ПО
    classifications = Classification.objects.all().filter(date_of_delete=None, visibility=True).order_by('id')

    return render(request, 'soft/catalog.html', {'soft_list':soft_list, 'photo_dict':photo_dict, 'count':count, 'modification':modification, 
    'search_query_name':search_query_name, 'soft_price':soft_price, 'soft_pricefrom':soft_pricefrom, 
    'soft_priceto':soft_priceto, 'tags_dict':tags_dict, 'classifications':classifications, 
    'classification_dict':classification_dict})


# Страница одного ПО
def software_page(request, id):

    # Хэш классификаций ПО
    classif = {}

    try:
        software = Software.objects.get( id = id )

        # Получаем список приложений данного ПО (ФАЙЛЫ, ФОТОГРАФИИ)
        software_img = software.get_addition()

        
        # Получаем список тегов данного ПО
        software_tag = software.get_tags()


        #  Для разрыва текста (скрытого и открытого)
        # Сплит строки по '\n' по первому вхождению - получаем массив элементов одной переменной
        list_descr = software.description.split('\n', 1)

         # Получаем список классификаций данного ПО
        classif = software.get_classifications()
        # dbl.log(str(classif))

        dbl.log("str(ar)")
        ar = software.get_area()
        dbl.log(str(ar))

            #   СТАРОЕ РЕШЕНИЕ
            # dbl.log(str(clas.get(classification_value__classification__name)))

            # if clas.get(classification_value__classification__name) == "Область применения" :

            #     classif["area"] = clas.get(classification_value__value)
            #     break

            # elif clas.get(classification_value__classification__name) == "Вид" :

            #     classif["type"] = clas.get(classification_value__value)
            #     break

            # elif clas.get(classification_value__classification__name) == "Тип использования" :

            #     classif["type_of_use"] = clas.get(classification_value__value)
            #     break


    except:
        raise Http404("ПО не найдено")

    return render(request, 'soft/software.html', {'software':software, 'software_img':software_img, 'classif':classif, 'list_descr':list_descr, 'software_tag':software_tag})





# Ф-ия составления списка избранных ПО
def favourites(request):

    if request.user.is_authenticated:

        client = request.user
        return redirect('software:catalog')
    else:
        pass


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
            for s in soft_photo:
                photo_dict[soft.id] = s


    # Получение списка всех видов ПО
    classifications = Classification.objects.all().filter(date_of_delete=None, visibility=True).order_by('id')

    return render(request, 'soft/catalog.html', {'soft_list':soft_list, 'photo_dict':photo_dict, 'count':count, 'modification':modification, 
    'search_query_name':search_query_name, 'soft_price':soft_price, 'soft_pricefrom':soft_pricefrom, 
    'soft_priceto':soft_priceto, 'tags_dict':tags_dict, 'classifications':classifications, 
    'classification_dict':classification_dict})





# Ф-ия добавления избранного
def add_favourite(request, software_id):

    try:
        
        if request.user.is_authenticated:

            client = request.user
            software = Software.objects.get( id = int(software_id) )

            fav = software.is_favourite(client)

            if fav:
                
                fav.delete()
                
            else:
                Favourite.objects.create(client=client, software=software)

            return redirect('software:catalog')
        else:
            pass

    except:
        pass

    return redirect('software:catalog')


    # return render(request, 'soft/catalog.html', {'soft_list':soft_list, 'photo_dict':photo_dict, 'count':count, 'modification':modification, 
    # 'search_query_name':search_query_name, 'soft_price':soft_price, 'soft_pricefrom':soft_pricefrom, 
    # 'soft_priceto':soft_priceto, 'tags_dict':tags_dict, 'classifications':classifications, 
    # 'classification_dict':classification_dict})
