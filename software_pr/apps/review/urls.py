from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    # path('', views.list_reviews, name = 'list_reviews'),
    path('new/', views.review_create, name = 'review_create'),
    path('review_create/', views.review_create_for_software, name = 'review_create_for_software'),
    # path('review_create/success/', views.review_success, name = 'review_success'),
    path('new/success/', views.review_success, name = 'review_success'),
    path('', views.list_review, name = 'list_review'),

    # path('review_create/', include([
    #     path('', views.review_create_for_software),
    #     path('success/', views.review_success, name = 'review_success') 
    # ])),

]