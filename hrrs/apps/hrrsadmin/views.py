#-*- coding: utf-8
from django.shortcuts import render, get_object_or_404

from hrrs.apps.news.models import Article
from hrrs.apps.jobs.models import Job

def home(request):
    article_list = Article.objects.filter(published=True).order_by('-modify_time')
    job_list = Job.objects.filter(opened=True).order_by('-modify_time')
    return render(request, 'hrrsadmin/homepage.html', {'article_list': article_list, 'job_list': job_list})