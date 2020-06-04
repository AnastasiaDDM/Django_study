from django.urls import path
# from discussion.views import discussions

from . import views

app_name = 'discussion'

urlpatterns = [

    path('<str:type>/<int:id>', views.discussions, name = 'discussions'),
    path('<str:base>/<int:id>/<str:type1>', views.discussion_create, name = 'discussion_create'),
    # path('', views.list_review, name = 'list_review'),
    # path('new/', views.review_create, name = 'review_create'),
    # # path('review_create/', views.review_create_for_software, name = 'review_create_for_software'),
    # path('new/success/', views.review_success, name = 'review_success'),
    # path('new/success/<str:type>/<int:id>', views.review_success, name = 'review_success'),
    # path('<int:id>/', views.review_page, name = 'review_page'),
]