from django.urls import path
from . import views
from django.conf.urls import include
app_name = 'pay'
urlpatterns = [
    path('gateway/', views.add_pay, name='add_pay'),
    path('success/', views.pay_success, name='pay_success'),
    path('failed/', views.pay_failed, name='pay_failed'),
    
# http://127.0.0.1:8000/pay/gateway?order_id=3&amount=1000

]