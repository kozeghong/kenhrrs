from django.conf.urls import url
from .views import show, myresume, resumetodo, createnew, createnew_success

urlpatterns = [
    url(r'^my/$', myresume, name='resumes_my'),
    url(r'^show/(\d+)/$', show, name='resumes_show'),
    url(r'^todo/$', resumetodo, name='resumes_todo'),
    url(r'^todo/byjob/(\d+)/$', resumetodo, name='resumes_todo_byjob'),
    url(r'^createnew/(\d+)/$', createnew, name='resumes_createnew'),
    url(r'^createnew/success/(\d+)/(\d+)/$', createnew_success, name='resumes_createnew_success'),
]