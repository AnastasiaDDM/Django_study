from django.urls import path
from . import views
from django.conf.urls import include
app_name = 'software'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:id>/', views.software_page, name = 'software_page'),
]