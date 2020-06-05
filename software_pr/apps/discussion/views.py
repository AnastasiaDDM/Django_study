from django.shortcuts import render, redirect
from django.template.loader import render_to_string
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
def discussion_create(request):

    client = ''
    exist_comments = False # Флаг о наличии комментариев у обсуждения, для выбора шаблона для вставки комментария
    result='' # Переменная шаблона ответа

    # Получение данных из формы в переменную
    form = Discussion_CommentForm(request.POST)

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            # Данные по умолчанию - код ответа
            data = {'status': 'error'}

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():

                id_software = form.cleaned_data['id_software']
                id_discussion = form.cleaned_data['id_discussion']

                new_disc = Discussion()

                # Добавление обсуждения
                if id_software:
                    software = Software.objects.get(id=id_software)
                    new_disc.software = software

                # Добавление комментария
                if id_discussion:
                    new_disc = Comment()
                    discussion = Discussion.objects.get(id=id_discussion)
                    new_disc.discussion = discussion

                    # Получение списка комментариев к данному обсуждению (для выбора шаблона ответа)
                    comment_list = Comment.objects.filter(date_of_delete=None, visibility=True, discussion=discussion).order_by('date')

                    if len(comment_list) >0:

                        exist_comments = True # Установка флага о наличии комментариев

                # Заполнение полей модели
                new_disc.name = form.cleaned_data['name']
                new_disc.email_phone = form.cleaned_data['email_phone'] 
                new_disc.content = form.cleaned_data['content']

                # Сохранение запроса (происходит тогда, когда все поля валидны)
                new_disc.save()

                if id_software:

                    result = render_to_string('discussion/pattern_form_discussion.html', {'disc':new_disc})

                if id_discussion:
                    
                    if exist_comments == False:

                        result = render_to_string('discussion/pattern_form_comment_with_button.html', {'comment':new_disc})

                    if exist_comments == True:

                        result = render_to_string('discussion/pattern_form_comment.html', {'comment':new_disc})

                data['status'] = 'success' 
                data['result'] = result
            else: # !!! Если ошибка, то отправляем ошибочные данные
                # !!! Быстро и некрасиво добавляем ошибки в ответ. Желательно для этого сделать отдельную функцию, так как тебе в нескольких местах придется этот код повторять
                data['error_text'] = '' # !!!!
                for v in form.errors.values(): # !!!!
                    data['error_text'] += v[0] + "<br>" # !!!!
                data['status'] = 'error' # !!!!

            return HttpResponse(json.dumps(data), content_type='application/json')

        except Exception as error:
            pass
            dbl.log("Ошибка работы " + str(error))

    return redirect('software:catalog')



