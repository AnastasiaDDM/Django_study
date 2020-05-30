from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
# from clients.models import Client
from django.contrib.auth.models import User
from user.models import *
# from user.managers import CustomUserManager
# from user.authentication import get_user_by_email_phone
# from user.authentication import *
import dbl
import re
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

# Ф-ия определния что именно передано в нее: номер телефона или эл.почта
def is_email(email_phone=None):
    # Проверка значения на емайл
    if re.match(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', str(email_phone)):
        return True
    return False


#todo  Нужно сделать правильную регистрацию по смс, в телеграмме есть инструкция
def Registration(request):
    form = RegisterForm()

    # Если пользователь авторизирован, то отправляем его на главную страницу
    if request.user.is_authenticated:
        return redirect('software:catalog')
    else:
        message =''
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            dbl.log('вью форма  '+str(form))
            if form.is_valid():
                # form.save()
                email = form.cleaned_data.get('email_phone')
                # password = CustomUser.objects.make_random_password(length=8, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
                # user.set_password(password)

                password = form.cleaned_data.get('password')
                # dbl.log('вью  '+str(email)+str(password))
                # user = CustomUserManager().get_user_by_email_phone(email_or_phone=email)
                user = CustomUser.get_user_by_email_phone(email_or_phone=email)


                # Пользователя с такими данными нет, значит можно регистрировать
                if user is None or str(user) is None:
                    # new_user = CustomUser()
                    email_phone = form.cleaned_data['email_phone']
                    # dbl.log('емайл '+str(email_phone))
                    is_email_bool = is_email(email_phone = email_phone)
                    # dbl.log('емайл 2 '+str(email_phone))

                    if is_email_bool:

                        # Сохранение запроса (происходит тогда, когда все поля валидны)
                        new_user = CustomUser.objects.create_user(email=email_phone, phone=None, password=password)
                    else:

                        # Сохранение запроса (происходит тогда, когда все поля валидны)
                        new_user = CustomUser.objects.create_user(email=None, phone=email_phone, password=password)

                    login(request, new_user, backend='user.authentication.Email_PhoneAuthBackend')

                    return redirect('software:catalog')
                else:
                    message ='Пользователь с такими данными уже есть'
        # else:
        #     form = RegisterForm()
        return render(request, 'registration/registration.html', {'form': form, 'message':message})


def Login(request):
    if request.user.is_authenticated:
        return redirect('software:catalog')
    else:
        form = LoginForm()
        message =''
        if request.method == 'POST':
            form = LoginForm(request.POST)
            dbl.log('вью форма  '+str(form))
            if form.is_valid():
                email = form.cleaned_data.get('email_phone')
                password = form.cleaned_data.get('password')
                dbl.log('вью  '+str(email)+str(password))
                user = authenticate(email_or_phone=email, password=password)
                dbl.log('вью юзер '+str(user))
                if user is not None:
                    dbl.log('вью юзер не ноль '+str(user)+str())
                    if user.is_active:
                        dbl.log('вью юзер активный'+str(user)+str())
                        login(request, user)
                        return redirect('software:catalog')
                else:
                    message ='Проверьте логин и пароль, и попробуйте снова'
        return render(request, 'registration/login.html', {'form': form, 'message':message})


def Logout(request):
    if request.user.is_authenticated:
        logout(request)                
    return redirect('software:catalog')


