from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from user.models import CustomUser
from software.models import Software, Favourite
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
    if request.user.is_authenticated:
        favourites = Software.get_favourites_by_user(request.user)
        return render(request, 'user/favourites.html', {'favourites':favourites})

# Полная очистка избранного
def favourites_clean(request):
    if request.user.is_authenticated:
        favourites = Favourite.get_favourites_by_user(request.user)
        for fav in favourites:
            fav.delete()
        return render(request, 'user/favourites.html', {'favourites':None})
