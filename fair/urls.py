"""fair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from nivagation.views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# set router for rest framework api

from nivagation.views import RoadViewSet, index, map

router = DefaultRouter()
router.register(r'road', RoadViewSet)

urlpatterns = [
    path('', index, name='index'),
    #path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('map/', map, name='map'),
    path('surface/', surface, name='surface'),
    path('service/', service, name='service'),
    path('about/', about, name='about'),
    path('new_index/', new_index, name='new_index'),
    path('small_map/', small_map, name='small_map'),
    path('contact/', contact, name='contact'),
    path('d3_map/', d3_map, name='d3_map'),
    path('project/', project, name='project'),
    path('surface/', surface, name='surface'),
    url(r'^api/', include(router.urls)),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
