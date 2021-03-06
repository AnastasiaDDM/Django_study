"""software_pr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from util import views as user_views
# import apps.util.views as util_views
# from user import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', s.index, name='index'),
    path('softwares/', include('software.urls')),
    path('articles/', include('article.urls')),
    path('reviews/', include('review.urls')),
    path('feedback/', include('feedback.urls')),
    path('user/', include('user.urls')),
    path('discussions/', include('discussion.urls')),
    path('pay/', include('pay.urls')),
    path('', include('main.urls')),
    path('order/', include('order.urls')),
    # path('company/', util_views.company, name = 'company'),
]


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)