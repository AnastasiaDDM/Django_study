from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
import dbl
import datetime
from django.db import models
from .forms import FeedbackForm
from django import forms

# Ф-ия работает со страницей обратной связи
def client_feedback(request):

    #  ЗДЕСЬ БУДЕТ ПРОВЕРКА АУТЕНТИФИКАЦИИ
    # if request.user.is_authenticated:
    #     pass
    #     client = User.objects.get(user=request.user)
    # else:
    #     client = ''

    client = ''

    # Получение данных из формы в переменную
    form = FeedbackForm(request.POST)

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():

                # Сохранение запроса (происходит тогда, когда все поля валидны)
                form.save()
                return redirect('feedback:feedback_success')

        except Exception as error:
            pass
            dbl.log("Ошибка работы с фидбеком" + str(error))

    return render(request, 'review/feedback.html', {'client':client, 'form': form})

# Ф-ия отображаения страницы успешного выполнения
def feedback_success(request):

    # Массив хлебных крошек
    list_crumb = [['Главная', 'software:catalog'], ['Заказать звонок', 'feedback:client_feedback']]

    message = "Ваша заявка на звонок принята! Вам перезвонят в ближайшее время"

    return render(request, 'common/successfull.html', {'message':message, 'list_crumb':list_crumb})
