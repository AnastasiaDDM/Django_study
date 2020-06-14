from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from user.models import CustomUser
from software.models import Software, Favourite, Download
from order.models import Order
import util.views
# from user.authentication import get_user_by_email_phone
from django import forms
from .forms import *
import dbl
import re

# Личные данные
def personal_data(request):

    if request.user.is_authenticated:
        return render(request, 'user/personal_data.html')

# Редактирование личных данных
def personal_data_edit(request):
    if request.user.is_authenticated:

        # Получение данных из формы в переменную
        form = PersonalForm(request.POST)

        # Получение данных из формы и сохранение в бд
        if request.method == "POST":
            try:
                user = request.user
                # Здесь автоматически проверяются все поля формы методами clean_...
                if form.is_valid():

                    # Заполнение полей модели
                    user.name = form.cleaned_data['name']
                    user.surname = form.cleaned_data['surname']
                    user.patronymic = form.cleaned_data['patronymic']
                    user.email = form.cleaned_data['email']
                    user.phone = form.cleaned_data['phone']
                    user.phone_second = form.cleaned_data['phone_second']
                    user.social = form.cleaned_data['social']
                    user.date_of_birth = form.cleaned_data['date_of_birth']
                    user.mailing = form.cleaned_data['mailing']

                    # Сохранение запроса (происходит тогда, когда все поля валидны)
                    user.save()
                    return redirect('user:personal_data')

            except:
                pass

        return render(request, 'user/personal_data_edit.html', {'form': form})


# Избранное
def favourites(request):
    # Получения пользователя
    user = CustomUser.get_user(request)
    dbl.log("1")

    if user:
        dbl.log("1")
        favourites = Software.get_favourites_by_user(user)
        dbl.log("1"+str(favourites))

        # Словарь главных фото
        photo_dict = {}
        dbl.log("1")
        for soft in favourites:

            # Получение главного фото
            soft_photo = soft.get_main_photo()

            if soft_photo is not None:

                # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
                for s in soft_photo:
                    dbl.log("1")
                    photo_dict[soft.id] = s
        dbl.log("1")
        response= render(request, 'user/favourites.html', {'favourites':favourites, 'user':user, 'photo_dict':photo_dict})
        return response


# Полная очистка избранного
def favourites_clean(request):
    # Получения пользователя
    user = CustomUser.get_user(request)

    if user:
        favourites = Favourite.get_favourites_by_user(user)
        for fav in favourites:
            fav.delete()
        return render(request, 'user/favourites.html', {'favourites':None})


# Загрузки
def downloads(request):
    # Получения пользователя
    user = CustomUser.get_user(request)

    if user:
        downloads = Software.get_downloads_by_user(user)

        # Словарь главных фото
        photo_dict = {}

        for soft in downloads:

            # Получение главного фото
            soft_photo = soft.get_main_photo()

            if soft_photo is not None:

                # Здесь перебор в цикле, но на самом деле в этом запросе всего 1 объект
                for s in soft_photo:
                    photo_dict[soft.id] = s

        response= render(request, 'user/downloads.html', {'downloads':downloads, 'user':user, 'photo_dict':photo_dict})
        return response