from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import CustomUser
from software.models import Software
import dbl

class Order(models.Model):

    original = 'org'
    modification = 'mod'
    buy = 'buy'

    KIND_ORDER = (
        (original, 'Оригинальная разработка'),
        (modification, 'Доработка'),
        (buy, 'Покупка'),
    )

    kind = models.CharField(max_length=3, choices=KIND_ORDER, default=buy, db_index=True)
    client = models.ForeignKey(CustomUser, on_delete = models.PROTECT, verbose_name='Клиент', related_name='order_client')
    software = models.ForeignKey(Software, on_delete = models.PROTECT, verbose_name='ПО', null=True, blank=True, related_name='order_software')
    cost = models.FloatField('Стоимость', validators=[MinValueValidator(0)])
    name = models.CharField('Наименование заказа', max_length = 200, null=True, blank=True)
    note = models.TextField('Примечание', null=True, blank=True)
    date = models.DateTimeField('Дата создания договора', auto_now_add=True, blank=True)
    starting_date = models.DateTimeField('Дата начала', null=True, blank=True)
    ending_date = models.DateTimeField('Дата окончания', null=True, blank=True)
    discount = models.FloatField('Скидка', null=True, blank=True, validators=[MinValueValidator(0)])
    license = models.DateTimeField('Дата окончания лицензии', blank=True, null=True)
    manager = models.ForeignKey(CustomUser, on_delete = models.PROTECT, verbose_name='Менеджер', null=True, blank=True, related_name='order_manager')
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)
    type_soft = models.CharField('Тип ПО', max_length = 200, null=True, blank=True)
    paid_amount = models.FloatField('Сумма оплат', null=True, blank=True, db_index=True, default=0)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    @staticmethod
    # Ф-ия получения списка избранных по клиенту
    def get_orders_by_user(client):
        return Order.objects.filter(client=client.id)


    # Метод возвращающий заказ или добавляет и возвращает его
    def get_order_or_create(self):

        try:
            # Получение уже имеющегося в бд заказа
            order = Order.objects.get( software=self.software, client=self.client )

        except:

            # Такого заказа нет, добавляем его в бд
            self.save()
            
            # Получение добавленного заказа
            order = Order.objects.get( software=self.software, client=self.client )

        return order

    # Ф-ия получения списка приложений
    def get_addition(self):

        # Получаем список приложений данного заказа (ФАЙЛЫ, ФОТОГРАФИИ)
        order_img = Order_Addition.objects.filter(order__id = self.id, date_of_delete=None)
        return order_img

    # Ф-ия получения главного фото заказа
    def get_main_photo(self):
        try:
            main_img = Order_Addition.objects.filter(order__id = self.id, date_of_delete=None, is_main=True)[:1]
            if not main_img:
                main_img = Order_Addition.objects.filter(order__id = self.id, date_of_delete=None)[:1]
        except:
            return None
        return main_img


    # Проверка принадлежности запрашиваемого заказа к текущему пользователю
    @staticmethod
    def get_order_by_client(order_id, client):

        try:
            # Получение уже имеющегося в бд заказа
            order = Order.objects.get( pk=order_id, client=client )

        except:
            return None

        return order

        
class Request(models.Model):
    name = models.CharField('Имя', max_length = 100, null=True, blank=True)
    client = models.ForeignKey(CustomUser, on_delete = models.PROTECT, verbose_name='Клиент', null=True, blank=True)
    phone = models.CharField('Телефон', max_length = 25)
    comment = models.TextField('Комментарий', null=True, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True, blank=True)
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Заявка на заказ'
        verbose_name_plural = 'Заявки на заказ'


class Order_Addition(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT, verbose_name='Заказ')
    name = models.CharField('Название', max_length = 50, null=True)
    kind = models.BooleanField('Тип (true - картинка)', default=True)
    size = models.BooleanField('Тип (true - большая картинка)', default=True)
    photo = models.ImageField('Фото', upload_to="order/", blank=True, null=True)
    file = models.FileField('Ссылка на файл', upload_to="file_order/", blank=True, null=True)
    is_main = models.BooleanField('Тип (true - главная)', default=False)      
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'



class Chat(models.Model):

    client = 'cl'
    manager = 'man'

    KIND_CHAT = (
        (client, 'Клиент'),
        (manager, 'Менеджер'),
    )

    order = models.ForeignKey(Order, on_delete = models.PROTECT, verbose_name='Заказ', related_name='chat_order')
    content = models.TextField('Текст', null=True, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True, blank=True)
    sender = models.CharField(max_length=3, choices=KIND_CHAT, default=manager, db_index=True)
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)

    def __str__(self):
        return str(self.order+ self.date)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Chat_Addition(models.Model):
    chat = models.ForeignKey(Chat, on_delete = models.PROTECT, verbose_name='Чат')
    kind = models.BooleanField('Тип (true - картинка)', default=True)
    photo = models.ImageField('Фото', upload_to="order/chat_photo/", blank=True, null=True)
    file = models.FileField('Ссылка на файл', upload_to="order/chat_file/", blank=True, null=True)     
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)

    def __str__(self):
        return self.chat

    class Meta:
        verbose_name = 'Приложение к чату'
        verbose_name_plural = 'Приложения к чату'