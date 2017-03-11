from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^resetArray$', views.resetArray),
    url(r'^setArray$', views.setArray),
    url(r'^findElement$', views.findElement),
]
