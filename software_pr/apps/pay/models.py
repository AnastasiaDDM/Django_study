from django.db import models
# import order.models as Order_models
from order.models import Order
import dbl
from django.db.models import Sum


class Pay(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT, verbose_name='Заказ', related_name='pay_order')
    amount = models.FloatField('Сумма')
    date = models.DateTimeField('Дата оплаты', auto_now_add=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    date_of_delete = models.CharField('Дата удаления', blank=True, max_length = 20, null=True, db_index=True)

    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    # Ф-ия считает сумму платежей переданного заказа
    @staticmethod
    def get_payment_of_order(order_id = 0):
        if order_id > 0:
            data = Pay.objects.filter(order=order_id).aggregate(Sum('amount'))
            if 'amount__sum' in data.keys():
                return int(data['amount__sum'])
        return 0
