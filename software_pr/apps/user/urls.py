from django.urls import path, re_path
from . import views
from django.conf.urls import include
from django.contrib.auth.views import LoginView
app_name = 'user'

urlpatterns = [
    # path('', views.list_article, name='list_article'),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('registration/', views.Registration, name='Registration'),
    # re_path('(?article_author=<article_author>[0-9]+)', views.list_article),
    # path('soft/', include('soft.urls')),
    # path('<int:id>/', views.software_page, name = 'software_page'),
]