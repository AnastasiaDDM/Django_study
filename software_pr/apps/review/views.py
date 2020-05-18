from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import *
from django.db.models import Q
import dbl
import datetime
from django.db import models
from .forms import ReviewForm
from django import forms
from software.models import Software
from review.models import Review

# Массив хлебных крошек
list_crumb_for_software = []




# Ф-ия списка статей
def list_review(request):
    review_list = Review.objects.all().filter(date_of_delete=None, visibility=True)

    # Получение пременных из формы поиска
    rating_to = request.GET.get('rating_to', '')
    rating_from = request.GET.get('rating_from', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    review_type = request.GET.get('review_type', '')

    # Фильтрация по дате начала отображения
    if date_from:

        date_from_for_db = datetime.datetime.strptime(date_from, '%d.%m.%Y')

        review_list = review_list.filter(date__gte=date_from_for_db)

    # Фильтрация по дате окончания отображения
    if date_to:
        
        date_to_for_db = datetime.datetime.strptime(date_to, '%d.%m.%Y')

        review_list = review_list.filter(date__lte=date_to_for_db)

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
    rating = [1,2,3,4,5]
    return render(request, 'review/reviews.html', {'review_list':review_list, 'rating': rating, 'rating_from':rating_from, 'rating_to':rating_to,
    'date_from':date_from, 'date_to':date_to, 'review_type':review_type })





# Ф-ия создания отзыва
def review_create(request):

    client = ''

    # Получение данных из формы в переменную
    form = ReviewForm(request.POST)
    dbl.log("Форма" + str(form))

    global list_crumb_for_software
    list_crumb_for_software = [['Главная', 'software:catalog'], ['Отзывы', 'review:list_review']]

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():

                
                # type_review = form.cleaned_data['kind']
                # if type_review == 'sof': # Отзыв о ПО
                #     dbl.log("ffff")
                #     id_soft = form.cleaned_data['software']
                #     dbl.log("Ошибка работы с по" + str(id_soft))
                #     form.software = Software.objects.get(id=id_soft)

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
    dbl.log("Форма" + str(form))

    # form.software = Software.objects.get(id=id_soft)
    software = Software.objects.get(id=id_soft)
    dbl.log("ПО аааааааа кебебебеб " + str(software))
    # dbl.log("ПО в форме " + str(form.software))


    global list_crumb_for_software
    # list_crumb_for_software = [['Главная', 'software:catalog'], ['Каталог', 'software:catalog'], [software.name,'software:software_page',software.id],
    # ['Написать отзыв', 'review:review_create_for_software',software.id]]

    list_crumb_for_software = [['Главная', 'software:catalog'], ['Каталог', 'software:catalog'], [software.name,'software:software_page',software.id]]

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            new_review = Review()

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():

                dbl.log("Ошибка работы с по" )

                # new_review = form.save(commit=False)
                
                
                # if type_review == 'sof': # Отзыв о ПО
                #     dbl.log("ffff")
                #     id_soft = form.cleaned_data['software']
                #     dbl.log("Ошибка работы с по" + str(id_soft))

            new_review.name = form.cleaned_data['name']
            new_review.email_phone = form.cleaned_data['email_phone']
            new_review.content = form.cleaned_data['content']
            new_review.star = form.cleaned_data['star']
            new_review.software = software
            # dbl.log("ПО в форме " + str(form.software))

                # new_review.software = software.id
                # dbl.log("ПО в форме " + str(new_review.software))

                # Сохранение запроса (происходит тогда, когда все поля валидны)
                # new_review.save()
            new_review.save()

            # return redirect('review:review_success')
            return redirect('review:review_success', type='software', id= software.id)

        except Exception as error:
            pass
            dbl.log("Ошибка работы с отзывом" + str(error))


    

    rating = [5,4,3,2,1]
    return render(request, 'review/review_create.html', {'client':client, 'form': form, 'rating': rating, 'list_crumb':list_crumb_for_software})


# # Ф-ия отображаения страницы успешного выполнения
# def review_success(request):

#     global list_crumb_for_software

#      # Массив хлебных крошек
#     list_crumb = list_crumb_for_software

#     dbl.log("строка крошек" + str(list_crumb_for_software))

#     if len(list_crumb_for_software) >2:

#         dbl.log("строка бе бебебебеб" )
        
#         soft_raw = list_crumb_for_software[2]

#         if len(soft_raw) == 3:
#             soft_id = soft_raw[2]
#             # list_crumb.append(['Написать отзыв', 'review:review_create_for_software', soft_id])
#             list_crumb.append(['Написать отзыв', 'review:review_create_for_software', soft_id])
#     else:
#         list_crumb.append(['Написать отзыв', 'review:review_create'])


#     dbl.log("новая строка крошек" + str(list_crumb))
#     # dbl.log("строка крошек" + str(list_crumb_for_software.append(['Написать отзыв', 'review:review_create_for_software'])))

#     message = "Спасибо за отзыв!"

#     return render(request, 'common/successfull.html', {'message':message, 'list_crumb':list_crumb})



# Ф-ия отображаения страницы успешного выполнения
def review_success(request, type='', id = 0):

    global list_crumb_for_software

     # Массив хлебных крошек
    # list_crumb = []
    list_crumb = list_crumb_for_software

    if len(type)>0 and id>0:

        if type == 'software':
            list_crumb.append(['Написать отзыв', 'software:review_create_for_software', id])

    else:
        list_crumb.append(['Написать отзыв', 'review:review_create'])

    message = "Спасибо за отзыв!"

    return render(request, 'common/successfull.html', {'message':message, 'list_crumb':list_crumb})

