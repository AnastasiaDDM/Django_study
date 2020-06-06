from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import CustomUser
from software.models import Software

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
    manager = models.ForeignKey(CustomUser, on_delete = models.PROTECT, verbose_name='Менеджер', null=True, blank=True, related_name='order_manager')
    date_of_delete = models.DateField('Дата удаления', null=True, blank=True, db_index=True)
    visibility = models.BooleanField('Видимость на сайте', default=True, db_index=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    @staticmethod
    # Ф-ия получения списка избранных по клиенту
    def get_orders_by_user(client):
        # return Software.objects.filter(classification__id = self.id, visibility=True).order_by('value')
        return Order.objects.filter(client=client.id)