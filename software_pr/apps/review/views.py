from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
import dbl
import datetime
from django.db import models
from .forms import ReviewForm
from django import forms
from software.models import Software

# Ф-ия создания отзыва
def review_create(request):

    client = ''

    # Получение данных из формы в переменную
    form = ReviewForm(request.POST)
    dbl.log("Форма" + str(form))

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":
        try:

            # Здесь автоматически проверяются все поля формы методами clean_...
            if form.is_valid():

                
                # type_review = form.cleaned_data['kind']
                # if type_review == 'sof': # Отзыв о ПО
                #     dbl.log("ffff")
                #     id_soft = form.cleaned_data['software']
                #     dbl.log("Ошибка работы с по" + str(id_soft))
                #     form.software = Software.objects.get(id=id_soft)

                # Сохранение запроса (происходит тогда, когда все поля валидны)
                form.save()
                return redirect('feedback:feedback_success')

        except Exception as error:
            pass
            dbl.log("Ошибка работы с отзывом" + str(error))

    rating = [5,4,3,2,1]
    return render(request, 'review/review_create.html', {'client':client, 'form': form, 'rating': rating})


# Ф-ия отображаения страницы успешного выполнения
def feedback_success(request):

    message = "Ваша заявка на звонок принята! Вам перезвонят в ближайшее время"

    return render(request, 'common/successfull.html', {'message':message})




