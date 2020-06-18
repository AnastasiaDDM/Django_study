from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from user.models import CustomUser
from software.models import Software, Favourite
from .models import *
from .forms import *
import datetime
import dbl




# Заказы
def orders(request):

    # Получения пользователя
    user = CustomUser.get_user(request)

    if user:

        # Получение неотфильтрованного списка заказов клиента
        orders = Order.get_orders_by_user(user)
        orders = orders.filter(date_of_delete=None, visibility=True)

        # Получение данных из формы в переменную
        form = Search_OrderForm(request.GET)

        if form.is_valid():
            try:

                # Получение пременных из формы поиска
                date_type = form.cleaned_data['date_type']
                date_from = form.cleaned_data['date_from']
                date_to = form.cleaned_data['date_to']
                month = form.cleaned_data['month']
                status_order = form.cleaned_data['status_order']
                type_order = form.cleaned_data['type_order']
                type_soft = form.cleaned_data['type_soft']
                number = form.cleaned_data['number']
                name = form.cleaned_data['name']
                unread_messages = form.cleaned_data['unread_messages']
                sort_param = form.cleaned_data['sort']
                if sort_param is None:
                    sort_param = ""
                count = form.cleaned_data['count']
                if count == "":
                    count = 10
                count = int(count)
                try:
                    page = int(form.cleaned_data['page'])
                except:
                    page = 1

                
                # Получение поля фильтрации по типу даты
                date_type_for_db = ""

                if date_type == 'date_type_buy':

                    date_type_for_db = "date"

                elif date_type == 'date_type_start':

                    date_type_for_db = "starting_date"

                elif date_type == 'date_type_end':

                    date_type_for_db = "ending_date"

                # Фильтрация по дате (при выборе типа даты поиска)
                if date_type and date_type != 'date_type_select_not_selected':

                    # Фильтрация по дате начала фильтрации
                    if date_from:

                        date_from_for_db = datetime.datetime.strptime(date_from, '%d.%m.%Y')
                        field_name = date_type_for_db+'__gte'

                        # Переменная вида : {поле в бд для фильтрации: значение фильтра}
                        kw = {field_name: date_from_for_db}
                        orders = orders.filter(**kw)

                    # Фильтрация по дате окончания фильтрации
                    if date_to:
                        
                        date_to_for_db = datetime.datetime.strptime(date_to, '%d.%m.%Y')
                        field_name = date_type_for_db+'__lte'

                        # Переменная вида : {поле в бд для фильтрации: значение фильтра}
                        kw = {field_name: date_to_for_db}
                        orders = orders.filter(**kw)

                    # Фильтрация по месяцу
                    if month and month != '0':

                        field_name = date_type_for_db+'__month'

                        # Переменная вида : {поле в бд для фильтрации: значение фильтра}
                        kw = {field_name: month}
                        orders = orders.filter(**kw)

                # Фильтрация по типу заказа
                if type_order:

                    # Получение типа заказа
                    type_order_value = type_order.split('type_order_')
                    orders = orders.filter(kind=type_order_value[1])

                #  СКОРЕЕ ВСЕГО НУЖНО ЭТО ПЕРЕДЕЛАТЬ ! ТАК КАК НАЗВАНИЯ ВИДА ПО могут измениться.
                # Фильтрация по типу ПО
                if type_soft and type_soft != 'type_soft_all':

                    type_soft_for_db = ""

                    if type_soft == 'type_soft_desc':

                        type_soft_for_db = "Настольное приложение"

                    elif type_soft == 'type_soft_site':

                        type_soft_for_db = "Сайт"

                    elif type_soft == 'type_soft_mobile':

                        type_soft_for_db = "Мобильное приложение"

                    orders = orders.filter(type_soft=type_soft_for_db)

                # Фильтрация по номеру(id) заказа
                if number and str(number).isdigit():
                    orders = orders.filter(pk=int(number))

                # Фильтрация по наименованию заказа
                if name:
                    orders = orders.filter(name__icontains=name)

                # Сортировка, показать по, перейти на страницу
                orders = util.views.sort_show_by(orders, sort_param, count, page )

            except Exception as error:
                pass

            # ЗДЕСЬ НУЖНО БУДЕТ СДЛЕАТЬ РЕДИРЕКТ НА ОБЩУЮ СТРАНИЦУ С ОПИСАНЕИМ ОШИБКИ И ССЫЛКАМИ НА ЛК, КАТАЛОГ И ТД
                dbl.log("Ошибка работы с заказами" + str(error))

        return render(request, 'order/orders.html', {'orders':orders, 'form':form, 'user':user})

    else:
        
        return redirect('software:catalog')




# Страница одного ПО
def order_page(request, id):

    # Объявление начальных значений переменных
    order_img = Q()
    main_photo = Q()
    list_note = []
    order = None

    try:
        # Проверка принадлежности запрашиваемого заказа к текущему пользователю
        # Получения пользователя
        user = CustomUser.get_user(request)

        if user:
            # Получение заказа
            order = Order.get_order_by_client(id, user)

        if order != None:

            # Получаем список приложений данного ПО (ФАЙЛЫ, ФОТОГРАФИИ)
            if order.kind == "buy":
                software = Software.objects.get( order_software = id )

                #  Получение главного фото
                main_photo_query = software.get_main_photo()
                # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
                for photo in main_photo_query:
                    main_photo = photo

                order_img = software.get_addition()
            else:
                #  Получение главного фото
                main_photo_query = order.get_main_photo()
                # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
                for photo in main_photo_query:
                    main_photo = photo

                order_img = order.get_addition()

            # Исключения главного фото (main_photo) из списка фото
            if order_img:
                order_img = order_img.exclude(pk=main_photo.id)

            #  Для разрыва текста (скрытого и открытого)
            # Сплит строки по '\n' по первому вхождению - получаем массив элементов одной переменной
            if order.note:
                list_note = order.note.split('\n', 1)

            # Получение текущего пользователя 
            user = CustomUser.get_user(request)
            
            return render(request, 'order/order.html', {'order':order,  'user':user, 'list_note':list_note, 'order_img':order_img, 'main_photo':main_photo})

    except:
        raise Http404("Заказ не найден")

    raise Http404("Заказ не найден")




# Ф-ия я заявки на заказ
def request_to_order(request):

    # Добавление клиента в заявку, если пользователь авторизован
    if request.user.is_authenticated:
        client = request.user
    else:
        client = ''

    # Получение данных из формы в переменную
    form = RequestForm(request.POST)

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():

                # Сохранение запроса (происходит тогда, когда все поля валидны)
                form.save()
                return redirect('order:request_success')

        except Exception as error:
            pass
            dbl.log("Ошибка работы" + str(error))

    return render(request, 'order/request_to_order.html', {'client':client, 'form': form})

# Ф-ия отображаения страницы успешного выполнения
def request_success(request):

    # Массив хлебных крошек
    list_crumb = [['Главная', 'main:index'], ['Оставить заявку', 'order:request_to_order']]

    message = "Ваша заявка на заказ принята! Вам перезвонят в ближайшее время"

    return render(request, 'common/successfull.html', {'message':message, 'list_crumb':list_crumb})



# Страница чата
def chat(request, id):

    # Объявление начальных значений переменных
    # order_img = Q()
    # main_photo = Q()
    # list_note = []
    order = None
    chat = None

    try:
        # Проверка принадлежности запрашиваемого заказа к текущему пользователю
        # Получения пользователя
        user = CustomUser.get_user(request)

        if user:
            # Получение заказа
            order = Order.get_order_by_client(id, user)
            # chat = order.chat

    except Exception as error:
            pass
            dbl.log("Ошибка работы" + str(error))

    return render(request, 'order/chat.html', {'order':order, 'chat':chat})



# Добавление сообщения в чат
def message_add_for_chat(request, id):

    order = None
    chat = None

    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)

        try:
            # Проверка принадлежности запрашиваемого заказа к текущему пользователю
            # Получения пользователя
            user = CustomUser.get_user(request)

            if user:
                # Получение заказа
                order = Order.get_order_by_client(id, user)
        except Exception as error:
            pass
            dbl.log("Ошибка работы" + str(error))


        if form.is_valid():

            new_chat = Chat()
            

            # addition_file = request.FILES['file']

            addition_file = request.FILES.getlist('file')

            dbl.log(str(addition_file))

            new_chat.order = order

            # new_chat.order = form.cleaned_data['order_id']
            new_chat.content = form.cleaned_data['content']
            new_chat.sender = "cl"

            # Сохранение сообщения чата (происходит тогда, когда все поля валидны)
            new_chat.save()
            dbl.log(str(new_chat.pk))

            # chat = Software.objects.get( order_software = new_chat.id )

            for file in addition_file:

                new_addition = Chat_Addition()


                new_addition.chat = new_chat
                new_addition.file = file
                new_addition.save()
                dbl.log(str(new_addition.pk))

    return redirect('order:chat', id=order.id )