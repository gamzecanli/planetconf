
from django.conf.urls import  patterns, include, url
from django.contrib import admin
from .views import configuration

app_name="planet"
urlpatterns = [
    url(r'^$',configuration, name="configuration"),

]
