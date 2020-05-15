from django.urls import path
from . import views
from review.views import review_create_for_software
from django.conf.urls import include
app_name = 'software'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:id>/', views.software_page, name = 'software_page'),
    path('<int:id_soft>/review_create/', review_create_for_software, name = 'review_create_for_software'),
]