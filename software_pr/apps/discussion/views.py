from django.shortcuts import render
from django.db import models
from discussion.models import *
import dbl
from django.http import Http404, HttpResponseRedirect, HttpResponse

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
                    dbl.log(str(d.id))

                    list_disc_id.append(d.id)


                comment_list = Comment.objects.filter(date_of_delete=None, visibility=True, discussion__in=list_disc_id).order_by('date')
                dbl.log(str(comment_list))

                
                for discussion in discussion_list:

                    dbl.log("диск "+str(discussion.id))
                    dbl.log("ooo "+str(discussion.content))

                    list_comment_for_one_disc = []

                    for comment in comment_list:

                        dbl.log("ooo "+str(comment.discussion.id))
                        
                        if comment.discussion == discussion:

                            list_comment_for_one_disc.append(comment)


                    # Добавляем ключ и значение в словарь
                    comments_dict[discussion.id] = list_comment_for_one_disc

                dbl.log(str(comments_dict))

                for c in comments_dict.values():

                    dbl.log("дададада "+str(c))
                
                dbl.log("ddd "+str(comments_dict.values()))

    except:
        raise Http404("Такого обсуждения нет, попробуйте позже")



    return render(request, 'discussion/discussions.html', {'discussion_list':discussion_list, 'comments_dict':comments_dict,
    'software':software})



