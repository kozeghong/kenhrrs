#-*- coding: utf-8
from django.conf.urls import url
from .views import flow, show, shownow

urlpatterns = [
    url(r'^flow/(\d+)/$', flow, name='workflows_flow'),
    url(r'^show/(\d+)/$', show, name='workflows_show'),
    url(r'^now/(\d+)/$', shownow, name='workflows_now'),
]