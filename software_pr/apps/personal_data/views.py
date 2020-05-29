from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from user.models import CustomUser
from user.authentication import get_user_by_email_phone
from django import forms
from .forms import *
import dbl
import re


def personal_data(request):
    if request.user.is_authenticated:
        dbl.log(str(request.user))
        return render(request, 'user/personal_data.html', {})

def personal_data_edit(request):
    dbl.log('dddddddd')
    if request.user.is_authenticated:
        dbl.log(str(request.user))
        # if request.method == 'POST':
        dbl.log('dddddddd')

        # Получение данных из формы в переменную
        form = PersonalForm(request.POST)
        dbl.log("Форма" + str(form))

            #  Получение данных из формы и сохранение в бд
        if request.method == "POST":
            try:

                # Здесь автоматически проверяются все поля формы методами clean_...
                if form.is_valid():
                    pass

                    # Сохранение запроса (происходит тогда, когда все поля валидны)
                    # form.save()
                    # return redirect('review:review_success')

            except Exception as error:
                pass
                dbl.log("Ошибка работы с отзывом" + str(error))

        return render(request, 'user/personal_data_edit.html', {'form': form,})

