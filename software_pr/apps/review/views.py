from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import *
from django.db.models import Q
import dbl
import datetime
import re
from django.db import models
from django import forms
from .forms import *
from software.models import Software
from review.models import Review

# Ф-ия списка статей
def list_review(request):
    review_list = Review.objects.all().filter(date_of_delete=None, visibility=True)

    # Получение данных из формы в переменную
    form = Search_ReviewForm(request.GET)
    dbl.log(str(form))


    
    try:
        # Здесь автоматически проверяются все поля формы методами clean_...
        if form.is_valid():
            pass

        # Получение пременных из формы поиска
        rating_to = form.cleaned_data['rating_to']
        rating_from = form.cleaned_data['rating_from']
        date_from = form.cleaned_data['date_from']
        date_to = form.cleaned_data['date_to']
        review_type = form.cleaned_data['review_type']
        dbl.log("мммм  "+str(date_from))
        dbl.log("мммм  "+str(date_to))
        # dbl.log("sss   "+str(form.date_to))

        # rating_to = request.GET.get('rating_to', '')
        # rating_from = request.GET.get('rating_from', '')
        # date_from_1 = request.GET.get('date_from', '')
        # date_to = request.GET.get('date_to', '')
        # dbl.log(str(date_from_1))

        # review_type = request.GET.get('review_type', '')
        # review_type_name = "Дополнительные возможности..."
        dbl.log("111111111 ddkjdkd "+str(re.match(r'^\d{1,2}\.\d{2}\.\d{4}$', str(date_from))))

        # Фильтрация по дате начала отображения
        if date_from:

            # date_from_for_db = datetime.datetime.strptime(str(date_from), '%d.%m.%Y')

            review_list = review_list.filter(date__gte=date_from)

        # Фильтрация по дате окончания отображения
        if date_to:
            
            # date_to_for_db = datetime.datetime.strptime(str(date_to), '%d.%m.%Y')

            review_list = review_list.filter(date__lte=date_to)

        # Фильтрация по начальной границе рейтинга
        if rating_from:

            review_list = review_list.filter(star__gte=rating_from)

        # Фильтрация по конечной границе рейтинга
        if rating_to:

            review_list = review_list.filter(star__lte=rating_to)

        # Фильтрация по дополнительным фильтрам
        if review_type:

                if review_type == 'with_content':

                    review_list = review_list.filter(~Q(content=''))
                    # review_type='С текстом комментария'

                if review_type == 'without_content':

                    review_list = review_list.filter(content='')
                    # review_type='Без текста комментария'
                    
        review_list = review_list.order_by('-date')




        # НЕ РАБОТАЕТ
        # Поля выбора отображения на странице (мгновенное изменение) пока не работает(
        count = int(request.GET.get('count', '10'))
        dbl.log(str(count)+"fffff")

        paginator = Paginator( review_list, count )

        try:
            page = int(request.GET.get('page', '1'))

        except:
            page = 1
        
        try:
            review_list = paginator.page(page)
            dbl.log(str(page))
            dbl.log("пагинация")
        except(EmptyPage, InvalidPage):
            review_list = paginator.page(paginator.num_pages) 
            dbl.log("!!пагинация")

    except Exception as error:
        pass
        dbl.log("Ошибка работы с отзывом" + str(error))

    rating = [1,2,3,4,5]
    return render(request, 'review/reviews.html', {'review_list':review_list, 'form':form, 'rating': rating })


# , 'rating_from':rating_from, 'rating_to':rating_to,
#     'date_from':date_from, 'date_to':date_to, 'review_type':review_type


# Ф-ия создания отзыва
def review_create(request):

    client = ''

    # Получение данных из формы в переменную
    form = ReviewForm(request.POST)
    dbl.log("Форма" + str(form))

    # global list_crumb_for_software
    list_crumb_for_software = [['Главная', 'software:catalog'], ['Отзывы', 'review:list_review']]

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():

                # Сохранение запроса (происходит тогда, когда все поля валидны)
                form.save()
                return redirect('review:review_success')

        except Exception as error:
            pass
            dbl.log("Ошибка работы с отзывом" + str(error))

    rating = [5,4,3,2,1]
    return render(request, 'review/review_create.html', {'client':client, 'form': form, 'rating': rating, 'list_crumb':list_crumb_for_software})



# Ф-ия создания отзыва
def review_create_for_software(request, id_soft):

    client = ''

    # Получение данных из формы в переменную
    form = ReviewForm(request.POST)

    software = Software.objects.get(id=id_soft)
    dbl.log("ПО аааааааа кебебебеб " + str(software))


    # global list_crumb_for_software
    # list_crumb_for_software = [['Главная', 'software:catalog'], ['Каталог', 'software:catalog'], [software.name,'software:software_page',software.id],
    # ['Написать отзыв', 'review:review_create_for_software',software.id]]

    list_crumb_for_software = [['Главная', 'software:catalog'], ['Каталог', 'software:catalog'], [software.name,'software:software_page',software.id]]

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            new_review = Review()

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():
                pass

            new_review.name = form.cleaned_data['name']
            new_review.email_phone = form.cleaned_data['email_phone']
            new_review.content = form.cleaned_data['content']
            new_review.star = form.cleaned_data['star']
            new_review.software = software

            # Сохранение запроса (происходит тогда, когда все поля валидны)
            new_review.save()

            return redirect('review:review_success', type='software', id= software.id)

        except Exception as error:
            pass
            dbl.log("Ошибка работы с отзывом" + str(error))

    rating = [5,4,3,2,1]
    return render(request, 'review/review_create.html', {'client':client, 'form': form, 'rating': rating, 'list_crumb':list_crumb_for_software})


# Ф-ия отображаения страницы успешного выполнения
def review_success(request, type='', id = 0):

     # Массив хлебных крошек
    list_crumb = []

    if len(type)>0 and id>0:

        if type == 'software':

            software = Software.objects.get(id=id)

            list_crumb = [['Главная', 'software:catalog'], ['Каталог', 'software:catalog'],
             [software.name,'software:software_page', id], ['Написать отзыв', 'software:review_create_for_software', id]]

            # list_crumb.append(['Написать отзыв', 'software:review_create_for_software', id])

    else:
        list_crumb = [['Главная', 'software:catalog'], ['Отзывы', 'review:list_review'], ['Написать отзыв', 'review:review_create']]
        # list_crumb.append(['Написать отзыв', 'review:review_create'])

    message = "Спасибо за отзыв!"

    return render(request, 'common/successfull.html', {'message':message, 'list_crumb':list_crumb})



# Страница одного отзыва
def review_page(request, id):

    # Хэш классификаций ПО
    # classif = {}
 
    try:
        this_object= Review.objects.get( id = id )

        # Получаем список приложений данного отзыва
        review_img = this_object.get_addition()

        software = Software()
        photo_dict = {}

        if this_object.software is not None:

            software = Software.objects.get(id=this_object.software.id)



            # soft_tags_list = soft.get_tags()

            if software:

                soft_photo = software.get_main_photo()

                # # Добавляем ключ и значение в словарь
                # tags_dict[soft.id] = soft_tags_list

                if soft_photo is not None:
                    dbl.log("колво "+str(soft_photo))
                    # if count(soft_photo) >1:
                    for s in soft_photo:
                        photo_dict[software.id] = s



        # dbl.log(str(software))

        
        # # Получаем список тегов данного ПО
        # software_tag = software.get_tags()


        # #  Для разрыва текста (скрытого и открытого)
        # # Сплит строки по '\n' по первому вхождению - получаем массив элементов одной переменной
        # list_descr = software.description.split('\n', 1)

        #  # Получаем список классификаций данного ПО
        # classif = software.get_classifications()
        # # dbl.log(str(classif))

    except:
        raise Http404("Отзыв не найден")
    
    rating = [1,2,3,4,5]
    return render(request, 'review/review.html', {'review':this_object, 'rating': rating, 'review_img':review_img, 'software':software,
    'photo_dict':photo_dict})
    # return render(request, 'soft/software.html', {'this_object':this_object, 'software_img':software_img, 'classif':classif, 'list_descr':list_descr, 'software_tag':software_tag})
