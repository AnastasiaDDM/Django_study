from django.urls import path, re_path
from . import views
from django.conf.urls import include
from personal_data.views import personal_data, personal_data_edit
app_name = 'user'

urlpatterns = [
    # path('', views.list_article, name='list_article'),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('registration/', views.Registration, name='Registration'),
    path('lk/', personal_data, name='personal_data'),  
    path('lk/edit', personal_data_edit, name='personal_data_edit'),
    # re_path('(?article_author=<article_author>[0-9]+)', views.list_article),
    # path('soft/', include('soft.urls')),
    # path('<int:id>/', views.software_page, name = 'software_page'),
]