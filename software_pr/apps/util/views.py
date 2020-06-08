from django.shortcuts import render
from software.models import *
from discussion.models import *
from django.template.loader import render_to_string
from django.conf import settings


# Ф-ия присоединения куки к ответу
def wrap_cookie(response, cookie):
    dbl.log("30" )

    key =""
    value =""
    max_age = None

    if cookie:
        dbl.log("31" )
        dbl.log(str(cookie) )
        dbl.log(str(response) )

        key = cookie.get('key')
        value = cookie.get('value')
        max_age = cookie.get('max_age')
        dbl.log("rrrrr"+str(key) )
        dbl.log(str(key) )
        dbl.log("sdsdss "+str(value) )
        dbl.log("bbbb  "+str(max_age) )

        # dbl.log(str(key+value+max_age) )

        if key and value:

            dbl.log("33 " + str(response.set_cookie(key, value, max_age=max_age)))

            # return response.set_cookie(key, value, max_age=max_age, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)
            return response.set_cookie(key, value, max_age=max_age)

    return response

#     # Получение списка похожих ПО
#     similar_list = software.get_similars()

#     # Хэш фотографий ПО
#     photo_dict = {}
#     result =''

#     for soft in similar_list:

#         soft_photo = soft.get_main_photo()

#         # Добавляем ключ и значение в словарь
#         if soft_photo is not None:
#             for s in soft_photo:
#                 photo_dict[soft.id] = s

#     result = render_to_string('common/pattern_similars.html', {'similar_list':similar_list, 'photo_dict':photo_dict})
#     return result


# # Ф-ия создания кода html для облака тегов к ПО
# def render_similars_tags(software):

#     # Получение списка тегов похожих ПО
#     similar_tags_list = software.get_similars_tags()
#     result =''

#     result = render_to_string('common/pattern_similars_tags.html', {'similar_tags_list':similar_tags_list})
#     return result


# # Ф-ия создания кода html обсуждений и их комментариев
# def render_discussion_comment(software, request, limit=0):

#     # Объявление переменных
#     list_disc_id = []
#     discussions_list = []
#     comments_dict = {}
#     result =''

#     if limit == 0 :

#         discussions_list = Discussion.objects.all().filter(date_of_delete=None, visibility=True, software=software.id).order_by('date')

#     if limit != 0 and str(limit).isdigit() :

#         discussions_list = Discussion.objects.all().filter(date_of_delete=None, visibility=True, software=software.id).order_by('date')[:int(limit)]

#     for d in discussions_list:

#         list_disc_id.append(d.id)

#     comment_list = Comment.objects.filter(date_of_delete=None, visibility=True, discussion__in=list_disc_id).order_by('date')
    
#     for discussion in discussions_list:

#         list_comment_for_one_disc = []

#         for comment in comment_list:
            
#             if comment.discussion == discussion:

#                 list_comment_for_one_disc.append(comment)

#         # Добавляем ключ и значение в словарь
#         comments_dict[discussion.id] = list_comment_for_one_disc
    
#     result = render_to_string('discussion/pattern_block_discussion.html', {'discussions_list':discussions_list,
#     'comments_dict':comments_dict,'software':software}, request=request)
#     return result