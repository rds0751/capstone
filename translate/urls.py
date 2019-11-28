from django.conf.urls import url
from django.urls import path, include, re_path

from translate import views

urlpatterns = [
    url(r'^$', views.translate_view, name='login_index'),
]
