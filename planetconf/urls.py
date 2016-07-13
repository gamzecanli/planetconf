
from django.conf.urls import  patterns, include, url
from django.contrib import admin
from planet.views import index

urlpatterns = [
    url(r'^planet/', include('planet.urls')),
    url(r'^admin/', admin.site.urls),

]
