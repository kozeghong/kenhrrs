from django.conf.urls import url
from .views import show

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(\d+)/$', show, name='show'),
    url(r'^publish/(\d+)/$', publish, name='publish'),
    url(r'^modify/(\d+)/$', modify, name='modify'),
    url(r'^createnew/$', createnew, name='createnew'),
    url(r'^board/$', board, name='board'),
]