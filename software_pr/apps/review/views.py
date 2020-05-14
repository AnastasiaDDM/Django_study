from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
import dbl
import datetime
from django.db import models
from .forms import ReviewForm
from django import forms

# Ф-ия создания отзыва
def review_create(request):

    #  ЗДЕСЬ БУДЕТ ПРОВЕРКА АУТЕНТИФИКАЦИИ
    # if request.user.is_authenticated:
    #     pass
    #     client = User.objects.get(user=request.user)
    # else:
    #     client = ''

    client = ''

    form = ReviewForm(request.POST)

    #  Получение данных из формы и сохранение в бд
    # if request.method == "POST":
    #     try:
    #         if form.is_valid():

    #             new_review = form.save(commit=False)
                
    #             if client != '':
    #                 new_review.client = str(request.POST['client'])

    #             if request.POST['name']:

    #                 new_review.name = str(request.POST['name'])
    #                 dbl.log(str(new_review.name))

    #             if request.POST['phone']:

    #                 new_review.phone = str(request.POST['phone'])
    #                 dbl.log("11")


    #             if request.POST['comment']:

    #                 new_review.comment = request.POST['comment']
    #                 dbl.log("111")

    #             # Сохранение запроса
    #             new_review.save()

    #             dbl.log("Не ошибка ")

    #             return redirect('feedback:feedback_success')

    #         else:
    #             dbl.log("Ошибка 1")

    #     except :
    #         pass
    #     dbl.log("Ошибка 2")

    # else:
    #     dbl.log("Ошибка 3")

    return render(request, 'review/review_create.html', {'client':client, 'form': form})


# Ф-ия отображаения страницы успешного выполнения
def feedback_success(request):

    message = "Ваша заявка на звонок принята! Вам перезвонят в ближайшее время"

    return render(request, 'common/successfull.html', {'message':message})




