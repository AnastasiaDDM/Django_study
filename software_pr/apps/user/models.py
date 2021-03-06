from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager
import secrets
from datetime import timedelta, datetime

class CustomUser(AbstractBaseUser, PermissionsMixin):

    CLIENT = 'CL'
    DEVELOPER = 'DEV'
    AUTHOR = 'AUT'
    ADMIN = 'ADM'

    KIND_USER = (
        (CLIENT, 'Клиент'),
        (DEVELOPER, 'Разработчик'),
        (AUTHOR, 'Автор'),
        (ADMIN, 'Админ'),
    )

    email = models.CharField('Электронная почта', max_length = 50, unique=True, default=None, null=True, blank=True)
    kind = models.CharField(max_length=3, choices=KIND_USER, default=CLIENT, db_index=True)  
    surname = models.CharField('Фамилия', max_length = 50, null=True, blank=True)
    name = models.CharField('Имя', max_length = 50, blank=True)
    patronymic = models.CharField('Отчество', max_length = 50, null=True, blank=True)
    phone = models.CharField('Телефон', max_length = 20, unique=True, null=True, blank=True)
    phone_second = models.CharField('Запасной телефон', max_length = 20, null=True, blank=True)
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    social = models.CharField('Социальные сети', max_length = 400, null=True, blank=True)
    comment = models.CharField('Комментарий', max_length = 900, null=True, blank=True)
    mailing = models.BooleanField('Рассылка на почту', default=False)
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)
    is_active = models.BooleanField('Активность', default=True)
    is_staff = models.BooleanField('Админ', default=False)
    guest_session = models.CharField('Сессия гостя', max_length = 80, unique=True, default=None, null=True, blank=True)
    # max_age = models.FloatField('Время действия кук', max_length = 20, default=None, null=True, blank=True)
    expires = models.DateField('Время действия кук', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.email:
            return self.email
        elif self.phone:
            return self.phone
        elif self.guest_session:
            return self.guest_session
        else:
            return "Неизвестный"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):

        full_name = '%s %s' % (self.name, self.surname)
        return full_name.strip()


    def get_short_name(self):

        return self.name

    @staticmethod
    def get_user_by_email_phone(email_or_phone):
        try:
            return CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))
        except :
            return None

    # Метод поиска пользователя по полю и значению
    @staticmethod
    def _get_user( field = None, value = None ):
        try:

            # Переменная вида : {поле в бд для фильтрации: значение фильтра}
            kw = {field: value}

            return CustomUser.objects.get(**kw)
            
        except :
            return None


    # Метод поиска пользователя по авторизации и по сессии
    @staticmethod
    def get_user( request ):

        # Объявление начальных значений
        user = None

        try:
            #  Авторизованный пользователь
            if request.user.is_authenticated:
                user = request.user

            # Поиск по сессии
            else:

                if request.COOKIES.get('guest_session'):
                    
                    user = CustomUser._get_user( field = 'guest_session', value= request.COOKIES.get('guest_session') )
                    
        except :
            return None
        
        return user



    #todo  Нужно сделать функции перекидывания избранного, заказов и пр. от гостя и к пользователю, если он работал гостем, а потом авторизовался.
    # Метод возвращающий пользователя, гостя или добавляет гостя и возвращает его
    @staticmethod
    def get_user_or_create(request):

        # Объявление начальных значений
        user = None
        cookie = {}
        session_string =""
        expires = None

        if request.user.is_authenticated:
            user = request.user
            # dbl.log('эзареган' )

        else:

            # dbl.log(' не эзареган' )

            if request.COOKIES.get('guest_session'):
                # dbl.log('есть такие куки' )
                try:
                    user = CustomUser._get_user( field = 'guest_session', value= request.COOKIES.get('guest_session') )
                # Такого пользователя с такими куками в бд нет
                except :
                    pass

            else:

                # Устанавливаем куки и добавляем пользователя в бд
                session_string = secrets.token_urlsafe(32) 

                # Срок хранения кук -10 лет
                expires = datetime.now() + timedelta(days=3650)

                # dbl.log('нет таких куки')

                # Добавления пользователя в бд
                user = CustomUser.objects.create_user(session=session_string, expires=expires)
                cookie = {'key': 'guest_session', 'value': user.guest_session, 'expires': user.expires}

        return user, cookie








