from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from phishing import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^get_url', views.get_url, name='get_url'),
]