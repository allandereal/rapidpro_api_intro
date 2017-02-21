from django.conf.urls import url
import views

__author__ = 'kenneth'

urlpatterns = [
    url(r'^$', views.index),
]