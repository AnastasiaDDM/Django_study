from django.db import models

class User(models.Model):

    CLIENT = 'CL'
    DEVELOPER = 'DEV'
    AUTHOR = 'AUT'

    KIND_USER = (
        (CLIENT, 'Клиент'),
        (DEVELOPER, 'Разработчик'),
        (AUTHOR, 'Автор'),
    )

    kind = models.CharField(max_length=3, choices=KIND_USER, default=CLIENT, db_index=True)  
    surname = models.CharField('Фамилия', max_length = 50)
    name = models.CharField('Имя', max_length = 50)
    patronymic = models.CharField('Отчество', max_length = 50)
    phone = models.CharField('Телефон', max_length = 20)
    phone_second = models.CharField('Запасной телефон', max_length = 20, blank=True)
    mail = models.CharField('Электронная почта', max_length = 50, blank=True)
    date_of_birth = models.DateField('Дата рождения', blank=True)
    date_of_delete = models.DateField('Дата удаления', blank=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def get__name_surname(art_author):

        author = User.objects.get( id = art_author )

        return author
