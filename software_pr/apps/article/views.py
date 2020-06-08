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
    art_list = Article.objects.all()

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

        art_list = art_list.filter(name__icontains=search_query_name, visibility=True, date_of_delete=None).order_by('-date_of_review')

    # Фильтрация по автору
    if art_author:

        if str(art_author).isdigit():

            art_list = art_list.filter(author__id=int(art_author), date_of_delete=None).order_by('-date_of_review')

            author = CustomUser.objects.get( id = art_author )
            art_author = str(author.name + " " + author.surname)

        else :

            art_list = art_list.filter((Q(author__name__icontains=art_author) | Q(author__surname__icontains=art_author) | Q(author__patronymic__icontains=art_author)), date_of_delete=None).order_by('-date_of_review')

        

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




# # НЕНУЖНАЯ Ф-ИЯ
# def list_article_by_author(request, author_id):
#     art_list = Article.objects.all()
#     # # printtypelist = PrintType.objects.all()
#     search_query_name = request.GET.get('article_name', '')
#     art_author = request.GET.get('article_author', '')
#     art_date_from = request.GET.get('article_date_from', '')
#     art_date_to = request.GET.get('article_date_to', '')
# #     art_date_to = request.GET.get('article_date_to', '')

# # article_author

#     # try:
#     #         art_author_id = get_object_or_404(User, pk=author_id)  

#     #     except expression as identifier:

#     #         art_author_id = None 


#     # if art_author_id is not None:

#     #         dbl.log("Андрей7777")
#     #         art_list = art_list.filter(author__id=art_author_id)
   
   
   


# 	# search_printtype = request.GET.get('searchprinttype', 'Не выбрано')	
# 	# ascordesc = request.GET.get('searchpriceascdesc', 'Сначала дешевые')
# 	# orderby = '-service_price'
# 	# if ascordesc == 'Сначала дорогие':
# 	# 	orderby = orderby
# 	# else:
# 	# 	orderby = 'service_price'
# 	# soft_list = Soft.objects.filter(soft_name="Кафе")
# 	# dbl.log("Андрей")
# 	# dbl.log(search_query_name)


#     if search_query_name:

#         dbl.log("Андрей11")
#         art_list = art_list.filter(name__icontains=search_query_name)

#     if art_author:

#         dbl.log("Андрей22222")
#         # art_list = art_list.filter(author__name__icontains=art_author).order_by('-date_of_review')
#         art_list = art_list.filter((Q(author__name__icontains=art_author) | Q(author__surname__icontains=art_author) | Q(author__patronymic__icontains=art_author)), date_of_delete=None).order_by('-date_of_review')


# 		# elif search_printtype != 'Не выбрано':
# 		# 	services_list = Service.objects.filter(service_printtype__printtype_name = search_printtype).order_by(orderby)
# 		# elif (search_query_name) and (searchprinttype != 'Не выбрано'):
# 		# 	services_list = Soft.objects.filter(service_name__icontains=search_query_name, service_printtype = search_printtype).order_by(orderby)
# 		# else:
# 		# 	services_list = Service.objects.all().order_by(orderby)
# 		# paginator = Paginator(services_list, 3)

# 		# try:
# 		# 	page = int(request.GET.get('page', 1))
# 		# except:
# 		# 	page = 1

# 		# try:
# 		# 	services = paginator.page(page)

# 		# except(EmptyPage, InvalidPage):
# 		# 	services = paginator.page(paginator.num_pages)


#     if art_date_from:
#         # d = datetime.datetime.strptime("04.01.2020 12:13", '%d.%m.%Y %I:%M')
#         date_from_for_db = datetime.datetime.strptime(art_date_from, '%d.%m.%Y')

#         art_list = art_list.filter(date_of_review__gte=date_from_for_db)


#     if art_date_to:
#         # d = datetime.datetime.strptime("04.01.2020 12:13", '%d.%m.%Y %I:%M')
#         date_to_for_db = datetime.datetime.strptime(art_date_to, '%d.%m.%Y')

#         art_list = art_list.filter(date_of_review__lte=date_to_for_db)


#     # inner_qs = soft_list.values('id')

#     # software_class = Software_Classification_Value.objects.filter(software__in = inner_qs)
#     # form = form_page(request.GET) # A form bound to the POST data
#     # if form.is_valid(): # All validation rules pass
#     #     count= form_page.cleaned_data.get("count").values()



#     # if form_page.is_valid():
#     #      count= form_page.cleaned_data.get("count")


#     count = int(request.GET.get('count', '10000'))
#     dbl.log(str(count)+"fffff")

#     paginator = Paginator( art_list, count )

#     try:
#         page = int(request.GET.get('page', '1'))

#     except:
#         page = 1
    
#     try:
#         art_list = paginator.page(page)
#         dbl.log(str(page))
#         dbl.log("пагинация")
#     except(EmptyPage, InvalidPage):
#         art_list = paginator.page(paginator.num_pages) 
#         dbl.log("!!пагинация")

#     return render(request, 'article/articles.html', {'art_list':art_list, 'search_query_name':search_query_name, 'art_author':art_author, 'art_date_from':art_date_from, 'art_date_to':art_date_to})




# def software_page(request, id):
#     try:
#         software = Software.objects.get( id = id )
#         # dbl.log(software.name)
#         # directions_list = Direction.objects.all()
#         software_img = Addition.objects.filter(software = software.id)

#     except:
#         raise Http404("ПО не найдено")

#     # dbl.log(software.name)
#     return render(request, 'soft/software.html', {'software':software, 'software_img':software_img})
