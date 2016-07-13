
from django.conf.urls import  patterns, include, url
from django.contrib import admin
from .views import index,tarih_yaz

app_name="planet"
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^conf',tarih_yaz, name="tarih_yaz"),

]
