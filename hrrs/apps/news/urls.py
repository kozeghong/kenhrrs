from django.conf.urls import url
from .views import index, show, publish, modify, createnew, board

urlpatterns = [
    url(r'^$', index, name='news_index'),
    url(r'^(\d+)/$', show, name='news_show'),
    url(r'^publish/(\d+)/$', publish, name='news_publish'),
    url(r'^modify/(\d+)/$', modify, name='news_modify'),
    url(r'^createnew/$', createnew, name='news_createnew'),
    url(r'^board/$', board, name='news_board'),
]