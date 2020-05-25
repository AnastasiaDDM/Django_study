from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager

# class User(models.Model):

#     CLIENT = 'CL'
#     DEVELOPER = 'DEV'
#     AUTHOR = 'AUT'

#     KIND_USER = (
#         (CLIENT, 'Клиент'),
#         (DEVELOPER, 'Разработчик'),
#         (AUTHOR, 'Автор'),
#     )

#     kind = models.CharField(max_length=3, choices=KIND_USER, default=CLIENT, db_index=True)  
#     surname = models.CharField('Фамилия', max_length = 50)
#     name = models.CharField('Имя', max_length = 50)
#     patronymic = models.CharField('Отчество', max_length = 50)
#     phone = models.CharField('Телефон', max_length = 20)
#     phone_second = models.CharField('Запасной телефон', max_length = 20, blank=True)
#     mail = models.CharField('Электронная почта', max_length = 50, blank=True)
#     date_of_birth = models.DateField('Дата рождения', blank=True)
#     date_of_delete = models.DateField('Дата удаления', blank=True, db_index=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'


#     # def get__name_surname(art_author):

#     #     author = User.objects.get( id = art_author )

#     #     return author




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
    # email = models.CharField('Электронная почта', max_length = 50)
    kind = models.CharField(max_length=3, choices=KIND_USER, default=CLIENT, db_index=True)  
    surname = models.CharField('Фамилия', max_length = 50, null=True, blank=True)
    name = models.CharField('Имя', max_length = 50, blank=True)
    patronymic = models.CharField('Отчество', max_length = 50, null=True, blank=True)
    phone = models.CharField('Телефон', max_length = 20, unique=True, null=True, blank=True)
    # phone = models.CharField('Телефон', max_length = 20, blank=True)
    phone_second = models.CharField('Запасной телефон', max_length = 20, null=True, blank=True)
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
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

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Sends an email to this User.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

