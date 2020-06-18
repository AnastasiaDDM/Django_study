from django.urls import path
from . import views
from review.views import review_create_for_software, review_success
# from discussion.views import discussions
from django.conf.urls import include
app_name = 'software'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:id>/', views.software_page, name = 'software_page'),
    path('<int:id_soft>/review_create/', review_create_for_software, name = 'review_create_for_software'),
    path('favourite/<int:software_id>', views.add_favourite, name='add_favourite'),  
    path('<int:software_id>/buy/', views.software_buy, name='software_buy'), 
    path('<int:software_id>/download', views.software_download, name='software_download'),
    path('<int:software_id>/download/add', views.add_download, name='add_download'),
    # path('download?id=<int:software_id>', views.software_send_file, name='software_send_file'),
        path('<int:software_id>/download/send_file', views.software_send_file, name='software_send_file'),
    # path('<int:id>/discussions', discussions, name = 'discussions'),
    # path('sort/', views.sort, name='sort'),

    # path('<int:id_soft>/review_create/success/', review_success, name = 'review_success'),
    # path('<int:id_soft>/', include('review.urls'))
]