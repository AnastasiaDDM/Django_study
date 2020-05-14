from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    # path('', views.list_reviews, name = 'list_reviews'),
    path('new/', views.review_create, name = 'review_create'),
    # path('success/', views.feedback_success, name = 'feedback_success'),

]