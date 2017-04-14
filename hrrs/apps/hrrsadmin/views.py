#-*- coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from hrrs.apps.news.models import Article
from hrrs.apps.jobs.models import Job

def home(request):
    article_list = Article.objects.filter(published=True).order_by('-modify_time')
    job_list = Job.objects.filter(opened=True).order_by('-modify_time')
    is_manage = False
    if request.user.is_authenticated():
        if request.user.role in ['H', 'A', 'E'] or request.user.is_superuser:
            is_manage = True
    return render(request, 'hrrsadmin/homepage.html', {'article_list': article_list, 'job_list': job_list, 'is_manage': is_manage})


@login_required
def admin_overview(request):
    if request.user.role in ['H', 'A', 'E'] or request.user.is_superuser:
        return render(request, 'hrrsadmin/admin-overview.html')
    else:
        return redirect(reverse('home'))