from django.urls import path, re_path
from . import views
from django.conf.urls import include
app_name = 'articles'

urlpatterns = [
    path('', views.list_article, name='list_article'),
    # re_path('(?article_author=<article_author>[0-9]+)', views.list_article),
    # path('soft/', include('soft.urls')),
    # path('<int:id>/', views.software_page, name = 'software_page'),
]