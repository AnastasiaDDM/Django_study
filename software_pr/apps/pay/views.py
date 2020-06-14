from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
import json
from .models import Pay
from order.models import Order
from .forms import PayForm
import dbl

# Ф-ия добавления платежа и принятия ответа от платежной системы
def add_pay(request):

    # Получение данных из формы в переменную
    form = PayForm(request.GET)
    data = { 'status': 'no' }

    if form.is_valid():

        try:
            pay = Pay()

            # Заполнение полей модели
            order_id = form.cleaned_data['order_id']
            order = Order.objects.get( id = int(order_id) )
            pay.order = order
            pay.amount = form.cleaned_data['amount']
            pay.save()
            
            # Получения суммы оплат по данному заказу и обновление paid_amount
            amount = Pay.get_payment_of_order(order.id)
            order.paid_amount = amount
            order.save()
            data = { 'status': 'ok' }

        # except :
        #     pass

        except Exception as error:
            pass
            dbl.log("Ошибка работы " + str(error))
    
    return HttpResponse(json.dumps(data), content_type='application/json')


# Ф-ия успешной оплаты
def pay_success(request):

    # todo
    # Нужно как-то отслеживать тип заказа и ПО, чтобы формировать ссылку для скачивания

    message = "Благодарим вас за доверие! Ваша оплата прошла успешно!"


    download_link = "скачать.ссылка"
    h1 = "Оплата прошла успешно"

    return render(request, 'common/successfull.html', {'message':message, 'download_link':download_link, 'h1':h1})


# Ф-ия неуспешной оплаты
def pay_failed(request):

    # todo
    # Нужно как-то отслеживать тип заказа и ПО, чтобы формировать ссылку для скачивания

    message = "К сожалению, оплата не прошла. Возможно вам стоит попробовать в следующий раз."

    return render(request, 'common/fail.html', {'message':message})