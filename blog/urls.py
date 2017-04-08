from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^about/', views.about, name='About'),
    url(r'^contact/', views.contact, name='Contact'),
]
