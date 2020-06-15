from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.company, name = 'company'),
    path('how_to_order/', views.how_to_order, name = 'how_to_order'),
    path('help/', views.help, name = 'help'),
    path('contacts/', views.contacts, name = 'contacts'),     
]