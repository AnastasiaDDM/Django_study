from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.db import models
from software.models import *
from django.db.models import Q
from django.core.paginator import *
import dbl
import re, random
from user.models import CustomUser
from user.forms import Register_by_email_phone_Form
import util.views
import json
from django.template.loader import render_to_string
from discussion.views import render_discussion_comment
from order.models import Order


# Ф-ия составления списка ПО
def catalog(request):
    soft_list = Software.objects.all().filter(date_of_delete=None, visibility=True)

    dbl.log("mmmmm")
    dbl.log("бббб"+str(request))

    # Получение пременных из формы поиска
    search_query_name = request.GET.get('soft_name', '')
    search_query_tags = request.GET.get('soft_tags', '')
    soft_price = request.GET.get('soft_price', '')
    soft_pricefrom = request.GET.get('soft_pricefrom', '')
    soft_priceto = request.GET.get('soft_priceto', '')
    modification = request.GET.get('modification', '')

    # Словарь для фильтра классификаций
    classification_dict = {}
    vertical_widget = None
    list_tags = []

    # Перебор всех пришедших аргументов
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
    # dbl.log(str(cond))
    # dbl.log(str(soft_list))

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

    # Фильтрация по списку тегов ПО
    if search_query_tags:

        # Сплит строки запроса
        dbl.log("ввввввв  " + str(search_query_tags))
        list_tags = re.split(r'[ ,]+', search_query_tags)
        dbl.log("ртртртрт  " + str(list_tags))

        # Фильтрация ПО по списку тегов
        soft_list = Software.get_softwares_by_tags(soft_list, list_tags)
        dbl.log("ddddddddd " + str(soft_list))

    # Хэш классификаций ПО
    tags_dict = {}
    photo_dict = {}

    for soft in soft_list:

        soft_tags_list = soft.get_tags()

        soft_photo = soft.get_main_photo()

        # Добавляем ключ и значение в словарь
        tags_dict[soft.id] = soft_tags_list

        if soft_photo is not None:

            # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
            for s in soft_photo:
                photo_dict[soft.id] = s

    # Получение текущего пользователя 
    user = CustomUser.get_user(request)

    # Получение списка всех видов ПО
    classifications = Classification.objects.all().filter(date_of_delete=None, visibility=True).order_by('id')

    # if request.is_ajax():
    #     dbl.log("hhhh")
    #     for soft in soft_list:
    #         dbl.log("---  " + str(soft))
    #     response = sort( request, soft_list)
    #     dbl.log("hhhh "+str(response))
    #     return response


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
    except(EmptyPage, InvalidPage):
        soft_list = paginator.page(paginator.num_pages) 

    # Составление вертикального виджета
    # Список типов виджетов
    choice_widget_list = ['popular', 'new']
    # Выбор типа
    choice_widget = random.choice(choice_widget_list)
    # dbl.log("виджеты " + str(choice_widget))

    # Популярные ПО
    if choice_widget == "popular":
        vertical_widget_all = Software.get_popular()
        # dbl.log("виджеты " + str(vertical_widget_all))

        if len(vertical_widget_all) > 6 :
            vertical_widget = random.sample(vertical_widget_all,6)
        else:
            vertical_widget = vertical_widget_all
        # dbl.log("виджеты " + str(vertical_widget))
    
    # Новые ПО
    elif choice_widget == "new":
        vertical_widget = Software.get_new()

    response = render(request, 'soft/catalog.html', {'soft_list':soft_list, 'photo_dict':photo_dict, 'count':count, 'modification':modification, 
    'search_query_name':search_query_name, 'soft_price':soft_price, 'soft_pricefrom':soft_pricefrom, 'list_tags':list_tags,
    'soft_priceto':soft_priceto, 'tags_dict':tags_dict, 'classifications':classifications, 
    'classification_dict':classification_dict, 'user':user, 'choice_widget':choice_widget, 'vertical_widget':vertical_widget})
    return response


def sort( request, soft_list, *args, **kwargs):
        # sorting articles by date and rating with ajax
        data = {}
        dbl.log("111")
        if request.is_ajax():
            dbl.log("22")
            dbl.log("22  " + str(request))
            dbl.log("22  " + str(soft_list))
            for soft in soft_list:
                dbl.log("88  " + str(soft))
            # soft_list = Software.objects.all().filter(date_of_delete=None, visibility=True)
            # soft_list = Software.objects.all().filter(date_of_delete=None, visibility=True)
            sort_param = request.GET.get('sortid')
            dbl.log("99 "+str(sort_param))
            # if sort_param in ('create_date', '-create_date', 'rate', '-rate'):
            soft_list = soft_list.order_by(sort_param)
            dbl.log("000")
            data['result'] = render_block_software(request, soft_list)
            # dbl.log("22  " + str(data))
            # return JsonResponse(data)
            dbl.log("33")
            return HttpResponse(json.dumps(data), content_type='application/json')
        return super().get(request, *args, **kwargs)






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

    # Строка фильтра для хлебных крошек
    str_filter_for_breadcrumb = ""

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
        classif, str_filter_for_breadcrumb = software.get_classifications()

        # Второстепенные объекты - похожие ПО
        similar_block = render_similars(software, id_widget="same_software")
        similar_tags_block = render_similars_tags(software)
        discussion_comment_block = render_discussion_comment(software, request, limit=5)

        # Получение текущего пользователя 
        user = CustomUser.get_user(request)
        
        return render(request, 'soft/software.html', {'software':software, 'software_img':software_img, 'main_photo':main_photo, 'classif':classif,
        'list_descr':list_descr, 'software_tag':software_tag, 'similar_block':similar_block, 'similar_tags_block':similar_tags_block,
        'discussion_comment_block':discussion_comment_block, 'user':user, 'str_filter_for_breadcrumb':str_filter_for_breadcrumb})


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
        dbl.log("заказ " + str(user))

        if user:

            # Объявление начальных значений
            order = None
            url_to_pay = ""

            software = Software.objects.get( id = int(software_id) )

            # Создание заказа
            new_order = Order()
            new_order.software = software
            new_order.client = user
            new_order.cost = software.price
            new_order.name = software.name
            # todo
            # Еще добавить тип ПО надо!
            # Еще добавить тип заказа надо!

            order = new_order.get_order_or_create()
            dbl.log("заказ " + str(order))

            if order:
                # Строка запроса к платежной системе
                url_to_pay = "/order_id=" + str(order.pk) + "&amount=" + str(order.cost)

            response = render(request, 'soft/buy.html', {'software':software, 'user':user, 'url_to_pay':url_to_pay})
            response = util.views.wrap_cookie(response, cookie)
            return response

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    return redirect('software:catalog')


# Ф-ия отображения страницы покупки
def software_download(request, software_id):

    form = Register_by_email_phone_Form()
    url_to_download = ""

    try:
        # Объявление начальных значений
        user = None
        cookie = {}

        # Получение текущего пользователя 
        user, cookie = CustomUser.get_user_or_create(request)

        if user:

            software = Software.objects.get( id = int(software_id) )

            # if software:
                # Строка запроса к платежной системе
                # url_to_download = "/software_id=" + str(software.pk) + "&amount=" + str(software.cost)


            response = render(request, 'soft/download.html', {'software':software, 'user':user})
            response = util.views.wrap_cookie(response, cookie)
            return response

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    return redirect('software:catalog')


# Ф-ия добавления избранного
def add_download(request, software_id):
    
    message =""
    download_link=""
    list_crumb =[]

    try:

        # Получения пользователя
        user = CustomUser.get_user(request)

        if user:

            software = Software.objects.get( id = int(software_id) )

            Download.objects.get_or_create(client=user, software=software)

            message = "Благодарим вас за доверие!"
            download_link = software.file
            h1 = "Успешная загрузка"
            list_crumb = [['Главная', 'software:catalog'], ['Каталог', 'software:catalog'], [software.name, 'software:software_page', software.id], ['Скачать бесплатно', 'software:software_download', software.id]]

            return render(request, 'common/successfull.html', {'message':message, 'download_link':download_link, 'h1':h1, 'list_crumb':list_crumb})

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))

    message = "К сожалению, что-то пошло не так. Возможно вам стоит попробовать в следующий раз."

    return render(request, 'common/fail.html', {'message':message})




# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ

# Ф-ия создания кода html для похожих ПО
def render_similars(software, id_widget=None, display_type="", widget_shell=True, show_more=""):

    # Получение списка похожих ПО
    similar_list = software.get_similars()

    # Ф-ия составления html кода горихонтальных виджетов
    return render_horizontal_widgets(similar_list, id_widget=id_widget, display_type=display_type, widget_shell=widget_shell, show_more=show_more)

def render_horizontal_widgets(list_soft, id_widget=None, display_type="", widget_shell=True, show_more=""):
# list_soft - список ПО, id_widget - id блока виджетов, display_type - скрытий или видимы блок, widget_shell - true/false наличие большого контейнера виджета

    photo_dict = {}
    result =''

    try:
        for soft in list_soft:

            soft_photo = soft.get_main_photo()

            # Добавляем ключ и значение в словарь
            if soft_photo is not None:
                for s in soft_photo:
                    photo_dict[soft.id] = s

    except Exception as error:
        pass
        dbl.log("Ошибка работы " + str(error))


    
    result = render_to_string('common/pattern_horizontal_widgets.html', {'list_soft':list_soft, 'photo_dict':photo_dict, 'id_widget':id_widget,
    'display_type':display_type, 'widget_shell':widget_shell, 'show_more':show_more})
    return result




# Ф-ия создания кода html для облака тегов к ПО
def render_similars_tags(software):

    # Получение списка тегов похожих ПО
    similar_tags_list = software.get_similars_tags()
    result =''

    result = render_to_string('common/pattern_similars_tags.html', {'similar_tags_list':similar_tags_list})
    return result

# Ф-ия создания кода html для блока ПО
def render_block_software(request, soft_list):

        # Хэш классификаций ПО
    tags_dict = {}
    photo_dict = {}

    for soft in soft_list:

        soft_tags_list = soft.get_tags()

        soft_photo = soft.get_main_photo()

        # Добавляем ключ и значение в словарь
        tags_dict[soft.id] = soft_tags_list

        if soft_photo is not None:

            # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
            for s in soft_photo:
                photo_dict[soft.id] = s

    # Получение текущего пользователя 
    user = CustomUser.get_user(request)

    # Получение списка тегов похожих ПО

    result =''

    result = render_to_string('soft/pattern_block_software.html', {'soft_list':soft_list, 'photo_dict':photo_dict, 'user':user})
    return result

