
from django.conf.urls import  patterns, include, url
from django.contrib import admin
from .views import index

app_name="planet"
urlpatterns = [
    url(r'', index, name="index"),

]
