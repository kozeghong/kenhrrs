#-*- coding: utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from markdown import markdown
from cgi import escape

from .models import Resume
from hrrs.apps.jobs.models import Job
from hrrs.apps.users.models import User


@login_required
def show(request, resume_id=None):
    resume = get_object_or_404(Resume, pk=resume_id)
    if request.user.role in ['H', 'A', 'E'] or request.user == resume.owner:
        resume.projexp = markdown(escape(resume.projexp))
        resume.workexp = markdown(escape(resume.workexp))
        is_manage = False
        if request.user.is_authenticated():
            if request.user.role in ['H', 'A', 'E'] or request.user.is_superuser:
                is_manage = True
        to_user_list = User.objects.filter(role__in=['H', 'A', 'E']).order_by("pk")
        
        return render(request, 'resumes/resumes-show.html', 
                        {
                            'resume': resume, 
                            'is_manage': is_manage, 
                            'to_user_list': to_user_list
                        }
                    )
    else:
        return redirect(reverse('resumes_my'))


@login_required
def myresume(request):
    myresume_list = Resume.objects.filter(owner=request.user).order_by('-date_created')
    return render(request, 'resumes/resumes-my.html', {'myresume_list': myresume_list})


@login_required
def resumetodo(request, job_id=None):

    if request.user.role not in ['H', 'A', 'E']:
        return redirect(reverse('resumes_my'))

    if job_id is not None:
        if request.user.role in ['H', 'A']:
            resumetodo_list = Resume.objects.filter(job__id=job_id).order_by('-date_created')
        elif request.user.role in ['E', ]:
            resumetodo_list = Resume.objects.filter(job__id=job_id).order_by('-date_created')
    elif job_id is None:
        if request.user.role in ['H', 'A']:
            resumetodo_list = Resume.objects.all().order_by('-date_created')
        elif request.user.role in ['E', ]:
            resumetodo_list = Resume.objects.all().order_by('-date_created')

    return render(request, 'resumes/resumes-todo.html', {'resumetodo_list': resumetodo_list})


@login_required
def createnew(request, job_id=None):
    job = get_object_or_404(Job, pk=job_id, opened=True)
    if request.method == 'POST':
        degree = request.POST.get('degree', "")
        graduationyear = request.POST.get('graduationyear', "")
        school = request.POST.get('school', "")
        faculty = request.POST.get('faculty', "")
        subject = request.POST.get('subject', "")
        projexp = request.POST.get('projexp', "")
        workexp = request.POST.get('workexp', "")

        if(degree == "")or(graduationyear == "")or(school == "")or(faculty == "")or(subject == ""):
            return render(request, 'resumes/resumes-createnew.html', {'job': job})

        resume = Resume()
        resume.job = job
        resume.owner = request.user
        resume.degree = degree
        resume.graduationyear = graduationyear
        resume.school = school
        resume.faculty = faculty
        resume.subject = subject
        resume.projexp = projexp
        resume.workexp = workexp
        resume.save()
        return redirect(reverse('resumes_createnew_success', args=[job_id, resume.pk]))
    return render(request, 'resumes/resumes-createnew.html', {'job': job})

@login_required
def createnew_success(request, job_id=None, resume_id=None):
    tips = {
            'tips_title': '简历投递成功！',
            'tips_memo': [
                u'<a href="'+reverse('resumes_show', args=[resume_id,])+u'">点击查看此简历</a>',
                u'<a href="'+reverse('resumes_my')+u'">点击查看我投递过的简历</a>',
            ]
        }
    return render(request, 'tips.html', tips)