#-*- coding: utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required  
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# import json

from .models import Job

def show(request, job_id=None):
    job = get_object_or_404(Job, pk=job_id, opened=True)
    return render(request, 'jobs/jobs-show.html', {'job': job})

def index(request):
    job_list = Job.objects.filter(opened=True).order_by('-modify_time')
    return render(request, 'jobs/jobs-list.html', {'job_list': job_list})

@login_required
def board(request):
    job_list = Job.objects.all().order_by('-pk')
    return render(request, 'jobs/jobs-board.html', {'job_list': job_list})

@login_required
def createnew(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        summary = request.POST.get('summary', None)
        description = request.POST.get('description', None)
        
        if(name is None)or(summary is None)or(description is None):
            return render(request, 'jobs/jobs-createnew.html')

        if(name == "")or(summary == "")or(description == ""):
            return render(request, 'jobs/jobs-createnew.html')

        job = Job()
        job.name = name
        job.summary = summary
        job.description = description
        job.createdby = request.user
        job.modifiedby = request.user
        job.save()
        return redirect(reverse('jobs_board'))
    return render(request, 'jobs/jobs-createnew.html')

@login_required
def modify(request, job_id=None):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        new_name = request.POST.get('name', None)
        new_summary = request.POST.get('summary', None)
        new_description = request.POST.get('description', None)
        
        if(new_name is None)or(new_summary is None)or(new_description is None):
            return redirect(reverse('jobs_modify', args=(job_id,)))

        if(new_name == "")or(new_summary == "")or(new_description == ""):
            return redirect(reverse('jobs_modify', args=(job_id,)))

        job.name = new_name
        job.summary = new_summary
        job.description = new_description
        job.modifiedby = request.user
        job.save()
        return redirect(reverse('jobs_board'))
    return render(request, 'jobs/jobs-edit.html', {'job': job})

@login_required
def opencontrol(request, job_id=None):
    job = get_object_or_404(Job, pk=job_id)
    job.opened = not job.opened
    # result = {'job_id': job.pk, 'opened': job.opened}
    job.save()
    # return HttpResponse(json.dumps(result), content_type='application/json')
    return redirect(reverse('jobs_board'))