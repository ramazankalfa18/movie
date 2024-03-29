"""film URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^(?P<id>\d+)/$', views.CategorySearch, name='CategorySearch'),
    path(r'^detail/(?P<id>\d+)/$', views.MovieShow, name='MovieShow'),
    path(r'^actor/$', views.Actors, name='Actor'),
    path(r'^actordetail/(?P<id>\d+)/$', views.actordetail, name='actordetail'),
    path(r'^CommentAdd/(?P<id>\d+)/$', views.CommentAdd, name='CommentAdd'),

]

admin.site.site_title = 'Film Otağı'
admin.site.site_header = 'Film Otağı'
admin.site.index_title = 'Film Otağına Hoşgeldiniz '
