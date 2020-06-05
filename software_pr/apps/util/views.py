from django.shortcuts import render
from software.models import *
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

