from django.urls import path, re_path
from . import views
from django.conf.urls import include
app_name = 'article'

urlpatterns = [
    path('', views.list_article, name='list_article'),
    path('<int:id>/', views.article_page, name = 'article_page'),
]