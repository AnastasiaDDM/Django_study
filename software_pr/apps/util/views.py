from django.shortcuts import render
from software.models import *
from discussion.models import *
from django.template.loader import render_to_string


# Ф-ия создания кода html для похожих ПО
def render_similars(software):

    # Получение списка похожих ПО
    similar_list = software.get_similars()

    # Хэш фотографий ПО
    photo_dict = {}
    result =''

    for soft in similar_list:

        soft_photo = soft.get_main_photo()

        # Добавляем ключ и значение в словарь
        if soft_photo is not None:
            for s in soft_photo:
                photo_dict[soft.id] = s

    result = render_to_string('common/pattern_similars.html', {'similar_list':similar_list, 'photo_dict':photo_dict})
    return result


# Ф-ия создания кода html для облака тегов к ПО
def render_similars_tags(software):

    # Получение списка тегов похожих ПО
    similar_tags_list = software.get_similars_tags()
    result =''

    result = render_to_string('common/pattern_similars_tags.html', {'similar_tags_list':similar_tags_list})
    return result


# Ф-ия создания кода html обсуждений и их комментариев
def render_discussion_comment(software, limit=0):

    # Объявление переменных
    list_disc_id = []
    discussions_list = []
    comments_dict = {}
    result =''

    if limit == 0 :

        discussions_list = Discussion.objects.all().filter(date_of_delete=None, visibility=True, software=software.id).order_by('date')

    if limit != 0 and str(limit).isdigit() :

        discussions_list = Discussion.objects.all().filter(date_of_delete=None, visibility=True, software=software.id).order_by('date')[:int(limit)]

    for d in discussions_list:

        list_disc_id.append(d.id)

    comment_list = Comment.objects.filter(date_of_delete=None, visibility=True, discussion__in=list_disc_id).order_by('date')
    
    for discussion in discussions_list:

        list_comment_for_one_disc = []

        for comment in comment_list:
            
            if comment.discussion == discussion:

                list_comment_for_one_disc.append(comment)

        # Добавляем ключ и значение в словарь
        comments_dict[discussion.id] = list_comment_for_one_disc
    
    result = render_to_string('discussion/pattern_block_discussion.html', {'discussions_list':discussions_list,
    'comments_dict':comments_dict,'software':software})
    return result