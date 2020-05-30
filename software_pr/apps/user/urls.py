from django.urls import path, re_path
from . import views
from django.conf.urls import include
import personal_data.views as personal
app_name = 'user'

urlpatterns = [
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('registration/', views.Registration, name='Registration'),
    path('lk/', personal.personal_data, name='personal_data'),  
    path('lk/edit', personal.personal_data_edit, name='personal_data_edit'),
    path('lk/favourites', personal.favourites, name='favourites'),
    path('lk/favourites/clean', personal.favourites_clean, name='favourites_clean'),
    # re_path('(?article_author=<article_author>[0-9]+)', views.list_article),
    # path('soft/', include('soft.urls')),
    # path('<int:id>/', views.software_page, name = 'software_page'),
]