# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
# from django.db.models import Q
# import dbl
# import datetime
# from django.db import models
# from feedback.models import *
# from .forms import FeedbackForm
# import re
# from django import forms

# from .models import *

# def client_feedback(request):

#     #  ЗДЕСЬ БУДЕТ ПРОВЕРКА АУТЕНТИФИКАЦИИ
#     # if request.user.is_authenticated:
#     #     pass
#     #     client = User.objects.get(user=request.user)
#     # else:
#     #     client = ''

#     client = ''


#     # if request.method == "POST":
#     #     dbl.log("Андрей")
#     #     # form = ReviewForm(request.POST)
#     #     # if form.is_valid():
#     #     try:
#     #         # new_feedback = form.save(commit=False)
            
#     #         if client != '':
#     #             client = client

#     #         if request.POST['name']:
#     #             name = request.POST['name']
#     #             dbl.log(str(name))

#     #         dbl.log("Андрей")

#     #         if request.POST['phone']:
#     #             phone = request.POST['phone']

#     #         if request.POST['comment']:
#     #             comment = request.POST['comment']

#     #         date = datetime.datetime.now()
#     #         dbl.log(str(date))
#     #         new_feedback = Feedback.objects.create(name = name, phone = phone, comment = comment, date = date)
#     #         dbl.log("Андрей111")
#     #         dbl.log(str(new_feedback))
#     #         # new_feedback.save()
#     #         # return redirect('reviews:client_message')
#     #         # else:
#     #         #     return render(request, 'reviews/add_review.html', {'form':form,'client':client,'services_list':services_list, 'doctors_list':doctors_list})
#     #     except:
#     #         pass
#     # else:
#     #     return render(request, 'review/feedback.html', {'client':client})
#     #     # pass
#     #     # form = ReviewForm()



#     #  Получение данных из формы и сохранение в бд
#     if request.method == "POST":

#         try:
#             dbl.log("Андрей")
#             form = FeedbackForm(request.POST)

#             dbl.log("!!!!! "+ str(form))

#             if form.is_valid():

#                 name = str(request.POST['name'])
#                 phone = str(request.POST['phone'])

#                 new_feedback = form.save(commit=False)
                
#                 if client != '':
#                     new_feedback.client = client

#                 if request.POST['name']:

#                     name = str(request.POST['name'])
#                     dbl.log("1")

#                     # # Проверка валидности значения имени
#                     # if re.match(r'[A-zА-я]+', name):

#                     new_feedback.name = name
#                     dbl.log(str(new_feedback.name))
#                     # else:

#                         # message = "Некорретное имя. Введите имя еще раз или оставьте это поле пустым"
#                     # return render(request, 'review/feedback.html', {'client':client, 'phone':phone})


#                 dbl.log("Андрей")

#                 if request.POST['phone']:
#                     new_feedback.phone = request.POST['phone']

#                 if request.POST['comment']:
#                     new_feedback.comment = request.POST['comment']

#                 new_feedback.date = datetime.datetime.now()
#                 dbl.log(str(new_feedback.date))

#                 dbl.log("Андрей111")
#                 dbl.log(str(new_feedback))

#                 # Сохранение запроса
#                 new_feedback.save()

#                 dbl.log("2")
#                 # form.add_error(name, "Некорретное имя. Введите имя еще раз или оставьте это поле пустым")
#                 dbl.log("3")
#                 # form.errors()
#                 dbl.log("4")
#                 # dbl.log("xxxx "+str(form.errors()))
#                 message = "Ваша заявка на звонок принята! Вам перезвонят в ближайшее время"

#                 # return redirect('software:catalog')
#                 dbl.log("не ошибка ")
#                 return render(request, 'common/successfull.html', {'message':message, 'form': form})

#             else:
#                 dbl.log("Ошибка")
#                 return render(request, 'review/feedback.html', {'client':client, 'phone':phone, 'form': form})

#         except :
#             pass

#     else:
#         dbl.log("Пук")
#         form = FeedbackForm()
#         return render(request, 'review/feedback.html', {'client':client, 'form': form})
#         # pass

#     dbl.log("упс")
#     return render(request, 'review/feedback.html', {'client':client, 'form': form})











from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
import dbl
import datetime
from django.db import models
from feedback.models import *
from .forms import FeedbackForm
import re
from django import forms

from .models import *

def client_feedback(request):

    #  ЗДЕСЬ БУДЕТ ПРОВЕРКА АУТЕНТИФИКАЦИИ
    # if request.user.is_authenticated:
    #     pass
    #     client = User.objects.get(user=request.user)
    # else:
    #     client = ''

    client = ''
    name = ''
    phone = ''
    comment = ''

    # if request.method == "POST":
    #     dbl.log("Андрей")
    #     # form = ReviewForm(request.POST)
    #     # if form.is_valid():
    #     try:
    #         # new_feedback = form.save(commit=False)
            
    #         if client != '':
    #             client = client

    #         if request.POST['name']:
    #             name = request.POST['name']
    #             dbl.log(str(name))

    #         dbl.log("Андрей")

    #         if request.POST['phone']:
    #             phone = request.POST['phone']

    #         if request.POST['comment']:
    #             comment = request.POST['comment']

    #         date = datetime.datetime.now()
    #         dbl.log(str(date))
    #         new_feedback = Feedback.objects.create(name = name, phone = phone, comment = comment, date = date)
    #         dbl.log("Андрей111")
    #         dbl.log(str(new_feedback))
    #         # new_feedback.save()
    #         # return redirect('reviews:client_message')
    #         # else:
    #         #     return render(request, 'reviews/add_review.html', {'form':form,'client':client,'services_list':services_list, 'doctors_list':doctors_list})
    #     except:
    #         pass
    # else:
    #     return render(request, 'review/feedback.html', {'client':client})
    #     # pass
    #     # form = ReviewForm()

    dbl.log("Ошибка -1")

    form = FeedbackForm(request.POST) # !!!!

    #  Получение данных из формы и сохранение в бд
    if request.method == "POST":

        try:
            dbl.log("Ошибка 0")


            if form.is_valid():

                name = str(request.POST['name'])
                phone = str(request.POST['phone'])

                new_feedback = form.save(commit=False)
                
                if client != '':
                    new_feedback.client = client

                if request.POST['name']:

                    name = str(request.POST['name'])
                    dbl.log("1")

                    new_feedback.name = name
                    dbl.log(str(new_feedback.name))
                 

                if request.POST['phone']:

                    phone = request.POST['phone']
                    new_feedback.phone = request.POST['phone']
                    dbl.log("11")


                if request.POST['comment']:

                    comment = request.POST['comment']
                    new_feedback.comment = request.POST['comment']
                    dbl.log("111")


                new_feedback.date = datetime.datetime.now()
                dbl.log(str(new_feedback.date))

                dbl.log("Андрей111")
                dbl.log(str(new_feedback))

                # Сохранение запроса
                new_feedback.save()

                #dbl.log("2")
                # form.add_error(name, "Некорретное имя. Введите имя еще раз или оставьте это поле пустым")
               # dbl.log("3")
                # form.errors()
                #dbl.log("4")
                #dbl.log("xxxx "+str(form.errors()))
                

                return redirect('feedback:feedback_success')
                dbl.log("Не ошибка ")
                # return redirect('common/successfull.html', {'message':message, 'form': form})
                # return render(request, 'common/successfull.html', {'message':message, 'form': form})

            else:
                dbl.log("Ошибка 1")
                #dbl.log(client)
                #dbl.log(form)
                #return render(request, 'review/feedback.html', {'client':client, 'phone':phone, 'form': form})

        except :
            pass
        dbl.log("Ошибка 2")
        #return render(request, 'review/feedback.html', {'client':client, 'form': form})

    else:
        dbl.log("Ошибка 3")
        form = FeedbackForm()
        # return render(request, 'review/feedback.html', {'client':client})
        # pass

    #dbl.log("упс")
    return render(request, 'review/feedback.html', {'client':client, 'phone':phone, 'name':name, 'comment':comment, 'form': form})  # !!!!



def feedback_success(request):

    message = "Ваша заявка на звонок принята! Вам перезвонят в ближайшее время"

    return render(request, 'common/successfull.html', {'message':message})
