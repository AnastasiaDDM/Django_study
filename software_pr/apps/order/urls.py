from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('request/', views.request_to_order, name='request_to_order'),
    path('<int:id>/', views.order_page, name = 'order_page'),
    path('<int:id>/chat', views.chat, name = 'chat'),
    path('<int:id>/chat/new', views.message_add_for_chat, name = 'message_add_for_chat'),
    
]