from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
    review_list = Review.objects.all()

    # Получение пременных из формы поиска
    rating_to = request.GET.get('rating_to', '')
    rating_from = request.GET.get('rating_from', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')


    # dbl.log("aaaaaa  "+ str(kwargs))
    # dbl.log("fffff  "+ str(art_author))

    # art_date_from = request.GET.get('article_date_from', '')
    # art_date_to = request.GET.get('article_date_to', '')

    # # НЕ РАБОТАЕТ
    # # Здась планируется обработка запроса списка статей по автору ( когда на карточке статьи
    # #  нажимают на автора, прогружается новый список статей с фильтром по автору )
    # dbl.log("fffff")
    # # auth_id = kwargs.get("author_id")
    # # if auth_id:

    # #     art_list = art_list.filter(author=auth_id, visibility=True, date_of_delete=None).order_by('-date_of_review')

            
    # # # Получаем список тегов данной статьи
    # # software_tag = Tag.objects.filter(softwares__id=software.id)


    # # Фильтрация по наименовании статьи
    # if search_query_name:

    #     art_list = art_list.filter(name__icontains=search_query_name, visibility=True, date_of_delete=None).order_by('-date_of_review')

    # # Фильтрация по автору
    # if art_author:

    #     if str(art_author).isdigit():

    #         dbl.log("111")

    #         art_list = art_list.filter(author__id=int(art_author), date_of_delete=None).order_by('-date_of_review')

    #         author = User.objects.get( id = art_author )
    #         art_author = str(author.name + " " + author.surname)

    #     else :

    #         dbl.log("333")
    #         art_list = art_list.filter((Q(author__name__icontains=art_author) | Q(author__surname__icontains=art_author) | Q(author__patronymic__icontains=art_author)), date_of_delete=None).order_by('-date_of_review')

        

    # # dbl.log(str(art_author))
    # # if str(art_author).isdecimal():
    # #     dbl.log("111")
    # #     # art_author = User.get__name_surname(art_author)

    # #     author = User.objects.get( id = art_author )

    # #     art_author = str(author.name + " " + author.surname)
    # #     dbl.log(str(art_author)+"fffff")

    # # # else:
    # # #     try:
    # # #         pass
    # # #     except ValueError:
    # # #         pass

    # Фильтрация по дате начала отображения
    if date_from:

        date_from_for_db = datetime.datetime.strptime(date_from, '%d.%m.%Y')

        review_list = review_list.filter(date_of_review__gte=date_from_for_db)

    # Фильтрация по дате окончания отображения
    if date_to:
        
        date_to_for_db = datetime.datetime.strptime(date_to, '%d.%m.%Y')

        review_list = review_list.filter(date_of_review__lte=date_to_for_db)


    # Фильтрация по начальной границе рейтинга
    if rating_from:

        review_list = review_list.filter(star__gte=rating_from)

    # Фильтрация по конечной границе рейтинга
    if rating_to:

        review_list = review_list.filter(star__lte=rating_to)

    # # НЕ РАБОТАЕТ
    # # Поля выбора отображения на странице (мгновенное изменение) пока не работает(
    # count = int(request.GET.get('count', '10000'))
    # dbl.log(str(count)+"fffff")

    # paginator = Paginator( art_list, count )

    # try:
    #     page = int(request.GET.get('page', '1'))

    # except:
    #     page = 1
    
    # try:
    #     art_list = paginator.page(page)
    #     dbl.log(str(page))
    #     dbl.log("пагинация")
    # except(EmptyPage, InvalidPage):
    #     art_list = paginator.page(paginator.num_pages) 
    #     dbl.log("!!пагинация")

    return render(request, 'review/reviews.html', {'review_list':review_list})





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

            return redirect('review:review_success')

        except Exception as error:
            pass
            dbl.log("Ошибка работы с отзывом" + str(error))


    

    rating = [5,4,3,2,1]
    return render(request, 'review/review_create.html', {'client':client, 'form': form, 'rating': rating, 'list_crumb':list_crumb_for_software})


# Ф-ия отображаения страницы успешного выполнения
def review_success(request):

    global list_crumb_for_software

     # Массив хлебных крошек
    list_crumb = list_crumb_for_software

    dbl.log("строка крошек" + str(list_crumb_for_software))

    if len(list_crumb_for_software) >2:

        dbl.log("строка бе бебебебеб" )
        
        soft_raw = list_crumb_for_software[2]

        if len(soft_raw) == 3:
            soft_id = soft_raw[2]
            # list_crumb.append(['Написать отзыв', 'review:review_create_for_software', soft_id])
            list_crumb.append(['Написать отзыв', 'review:review_create_for_software', soft_id])
    else:
        list_crumb.append(['Написать отзыв', 'review:review_create'])


    dbl.log("новая строка крошек" + str(list_crumb))
    # dbl.log("строка крошек" + str(list_crumb_for_software.append(['Написать отзыв', 'review:review_create_for_software'])))

    message = "Спасибо за отзыв!"

    return render(request, 'common/successfull.html', {'message':message, 'list_crumb':list_crumb})




