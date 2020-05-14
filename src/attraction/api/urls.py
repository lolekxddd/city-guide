from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include, url
from .views import AttractionRUDView, AttractionAPIView
urlpatterns = [
    url(r'^$', AttractionAPIView.as_view(), name='att_create'),
    url(r'^(?P<pk>\d+)/$', AttractionRUDView.as_view(), name='att_rud')
]