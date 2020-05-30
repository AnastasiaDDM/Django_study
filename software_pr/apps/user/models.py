from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager

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

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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







