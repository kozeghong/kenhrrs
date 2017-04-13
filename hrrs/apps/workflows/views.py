#-*- coding: utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import json

from .models import Workflow
from hrrs.apps.resumes.models import Resume
from hrrs.apps.users.models import User

@login_required
def flow(request, resume_id=None):
    resume = get_object_or_404(Resume, pk=resume_id)
    if request.user.role not in ['H', 'A', 'E']:
        return redirect(reverse('resumes_show', args=[resume.pk,]))

    wf_curr = Workflow.objects.filter(resume__id=resume_id).order_by('-time').first()

    if request.method == 'POST':
        title = request.POST.get('title', "")
        detail = request.POST.get('detail', "")
        to_user_id = request.POST.get('to_user_id', "")

        if(title == "")or(detail == "")or(to_user_id == ""):
            return redirect(reverse('resumes_show', args=[resume.pk,]))

        to_user = get_object_or_404(User, pk=to_user_id)

        nextfw = Workflow()
        nextfw.resume = resume
        nextfw.title = title
        nextfw.detail = detail
        nextfw.to_user = to_user
        nextfw.from_user = request.user

        if wf_curr:
            nextfw.prevwf = wf_curr
        else:
            nextfw.prevwf = None;
        
        nextfw.save()

        return redirect(reverse('resumes_show', args=[resume.pk,]))

    return redirect(reverse('resumes_show', args=[resume.pk,]))


@login_required
def show(request, resume_id=None):
    workflow_list = Workflow.objects.filter(resume__id=resume_id).order_by('-time')
    if workflow_list.exists():
        result = {
            'exists': True,
            'workflows': []
        }
        for workflow in workflow_list.iterator():
            result['workflows'].append({
                'id': workflow.pk,
                'status': workflow.title,
                'time': workflow.time.strftime('%Y-%m-%d %H:%M:%S'),
                'from_user': workflow.from_user.nickname+'('+workflow.from_user.email+')',
                'comment': workflow.detail,
                'to_user': workflow.to_user.nickname+'('+workflow.to_user.email+')',
                'resume': workflow.resume.pk,
                'prevwf': workflow.prevwf and workflow.prevwf.pk or None,
            })
        return HttpResponse(json.dumps(result), content_type='application/json')
    return HttpResponse(json.dumps({'exists': False}), content_type='application/json')


@login_required
def shownow(request, resume_id=None):
    workflow = Workflow.objects.filter(resume__id=resume_id).order_by('-time').first()
    if workflow:
        result = {
            'exists': True,
            'id': workflow.pk,
            'status': workflow.title,
            'time': workflow.time.strftime('%Y-%m-%d %H:%M:%S'),
            'from_user': workflow.from_user.nickname+'('+workflow.from_user.email+')',
            'comment': workflow.detail,
            'to_user': workflow.to_user.nickname+'('+workflow.to_user.email+')',
            'resume': workflow.resume.pk,
            'prevwf': workflow.prevwf and workflow.prevwf.pk or None,
        }
        return HttpResponse(json.dumps(result), content_type='application/json')
    return HttpResponse(json.dumps({'exists': False}), content_type='application/json')