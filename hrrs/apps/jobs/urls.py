from django.conf.urls import url
from .views import index, show, opencontrol, modify, createnew, board

urlpatterns = [
    url(r'^$', index, name='jobs_index'),
    url(r'^(\d+)/$', show, name='jobs_show'),
    url(r'^opened/(\d+)/$', opencontrol, name='jobs_opencontrol'),
    url(r'^modify/(\d+)/$', modify, name='jobs_modify'),
    url(r'^createnew/$', createnew, name='jobs_createnew'),
    url(r'^board/$', board, name='jobs_board'),
]