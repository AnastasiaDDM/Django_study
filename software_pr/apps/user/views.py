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
import secrets

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


# Метод возвращающий пользователя, гостя или добавляет гостя и возвращает его
def get_user(request):

    dbl.log("11" )

    user = CustomUser()
    cookie = {}
    session_string =""
    max_age = None

    if request.user.is_authenticated:
        user = request.user
        dbl.log('эзареган' )
        # photo_dict[software.id] = s
        

    else:

        dbl.log(' не эзареган' )

        if request.COOKIES.get('guest_session'):
            dbl.log('есть такие куки' )
            try:
                dbl.log('111111')
                user = CustomUser.get_user( field = 'guest_session', value= request.COOKIES.get('guest_session') )
                dbl.log('22222')

            # Такого пользователя в бд нет, нужно добавить 
            except :
                dbl.log('3333')
                session_string = request.COOKIES.get('guest_session')
                dbl.log(str(session_string))
                max_age = 365 * 12 * 3600 * 2
                # Добавления пользователя в бд
                user = CustomUser.objects.create_user(session=session_string, max_age=max_age)
            # dbl.log('есть такие куки' +str(user) )

        else:

            # Устанавливаем куки и добавляем пользователя в бд
            session_string = secrets.token_urlsafe(32) 
            dbl.log(str(session_string))
            # Срок хранения кук -2 года
            max_age = 365 * 12 * 3600 * 2

            dbl.log('нет таких куки')

            # Добавления пользователя в бд
            user = CustomUser.objects.create_user(session=session_string, max_age=max_age)
            # dbl.log('нет таких куки' +str(user) )

    # dbl.log(str(user))
    cookie = {'key': 'guest_session', 'value': user.guest_session, 'max_age': user.max_age}
    return user, cookie


