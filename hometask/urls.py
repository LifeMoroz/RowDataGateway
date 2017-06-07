"""hometask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import hometask.gof
from hometask import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', hometask.gof.ProfileController.get, name='profile'),
    url(r'^auth/$', views.UserController.auth, name='auth'),
    url(r'^news_list/$', views.NewsList.get, name='news_list'),
    url(r'^method_list/$', views.TMView.get, name='method_list'),
    url(r'^ask/$', views.QView.dispatch, name='ask_view')
]
