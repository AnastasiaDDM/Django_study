from django.shortcuts import render, redirect
from django.db import models
from discussion.models import *
import dbl
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import Discussion_CommentForm
import json

# Обсуждения 
def discussions(request, type='', id = 0):
    # if request.user.is_authenticated:
        # favourites = Software.get_favourites_by_user(request.user)

    try:

        if len(type)>0 and id>0:

            if type == 'softwares':

                software = Software.objects.get( id = id )

                list_disc_id = []

                # Хэш комментариев к обсуждениям 
                comments_dict = {}

                discussion_list = Discussion.objects.all().filter(date_of_delete=None, visibility=True, software=id).order_by('date')

                for d in discussion_list:
                    # dbl.log(str(d.id))

                    list_disc_id.append(d.id)


                comment_list = Comment.objects.filter(date_of_delete=None, visibility=True, discussion__in=list_disc_id).order_by('date')
                # dbl.log(str(comment_list))

                
                for discussion in discussion_list:

                    # dbl.log("диск "+str(discussion.id))
                    # dbl.log("ooo "+str(discussion.content))

                    list_comment_for_one_disc = []

                    for comment in comment_list:

                        # dbl.log("ooo "+str(comment.discussion.id))
                        
                        if comment.discussion == discussion:

                            list_comment_for_one_disc.append(comment)


                    # Добавляем ключ и значение в словарь
                    comments_dict[discussion.id] = list_comment_for_one_disc

                # dbl.log(str(comments_dict))

                # for c in comments_dict.values():

                #     dbl.log("дададада "+str(c))
                
                # dbl.log("ddd "+str(comments_dict.values()))

    except:
        raise Http404("Такого обсуждения нет, попробуйте позже")



    return render(request, 'discussion/discussions.html', {'discussion_list':discussion_list, 'comments_dict':comments_dict,
    'software':software})




# Ф-ия создания обсуждения
def discussion_create(request, base='', id = 0, type1=''):

    dbl.log("v[v[[v[v[v")

    client = ''

    # Получение данных из формы в переменную
    form = Discussion_CommentForm(request.POST)
    dbl.log("Форма" + str(form))


    # param = request.POST.get('time')

    # global list_crumb_for_software
    # list_crumb_for_software = [['Главная', 'software:catalog'], ['Отзывы', 'review:list_review']]

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            if len(base)>0 and id>0 and len(type1)>0:

                if base == 'softwares' or base == 'discussions':

                    new_disc = Discussion()

                    if type1 == 'new_comment':

                        new_disc = Comment()

                    if base == 'softwares':

                        software = Software.objects.get( id = id )
                        new_disc.software = software

                    if base == 'discussions':

                        discussion = Discussion.objects.get( id = id )
                        new_disc.discussion = discussion


                    data = { 'status': 'success' }    

                    # Здесь автоматически проверяются все поля формы методами clean_...
                    if form.is_valid():

                        # Заполнение полей модели
                        new_disc.name = form.cleaned_data['name']
                        new_disc.email_phone = form.cleaned_data['email_phone'] 
                        new_disc.content = form.cleaned_data['content']
                        
                        dbl.log("аааааа " + str(new_disc))

                        # Сохранение запроса (происходит тогда, когда все поля валидны)
                        new_disc.save()

                        data['result'] = '<div class="margin_top_07em comment_roll" id = "comment_roll_1" data-target="dis_{{disc.id}}"><a class="link_style_border"><i class="far fa-comments discussion_icon_com" aria-hidden="true"></i>Комментарии ({{comments|length}})</a></div> '

            # return redirect('discussion:discussions', {'softwares', software.id} )

            # return render(request, 'discussion/discussions.html', {'discussion_list':discussion_list, 'comments_dict':comments_dict,
    # 'software':software})

            # rating = [5,4,3,2,1]
            # return render(request, 'review/review_create.html', {'client':client, 'form': form, 'rating': rating})

            return HttpResponse(json.dumps(data), content_type='application/json')

        except Exception as error:
            pass
            dbl.log("Ошибка работы с отзывом" + str(error))

    rating = [5,4,3,2,1]
    return render(request, 'review/review_create.html', {'client':client, 'form': form, 'rating': rating})



