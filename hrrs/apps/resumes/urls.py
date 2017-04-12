from django.conf.urls import url
from .views import show, myresume, resumetodo, createnew

urlpatterns = [
    url(r'^my/$', myresume, name='resumes_my'),
    url(r'^show/(\d+)/$', show, name='resumes_show'),
    url(r'^resumetodo/$', resumetodo, name='resumes_todo'),
    url(r'^resumetodo/byjob/(\d+)/$', resumetodo, name='resumes_todo_byjob'),
    url(r'^createnew/(\d+)/$', createnew, name='resumes_createnew'),
]