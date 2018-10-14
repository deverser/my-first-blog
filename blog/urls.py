from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    ]