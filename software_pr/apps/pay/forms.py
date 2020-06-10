from django import forms
# Импорт общего приложения 
import util.forms
from django.core.exceptions import ValidationError
from .models import Order
import dbl

# Форма элементов для поиска заказов
class PayForm(forms.Form):

    amount = forms.FloatField()
    order_id = forms.CharField()

    # #  Ф-ии проверки валидности полей
    def clean_order_id(self):
        
        order_id = self.cleaned_data['order_id']
        dbl.log("000  "+str(order_id))

        try:
            order = Order.objects.get( id = int(order_id) )
            dbl.log("00000 "+str(order))
        except:
            raise ValidationError("Такого заказа нет, вы не можете его оплатить")

        return order_id
