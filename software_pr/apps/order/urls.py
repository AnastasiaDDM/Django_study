from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('request/', views.request_to_order, name='request_to_order'),
]