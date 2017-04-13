#-*- coding: utf-8
from django.db import models

from hrrs.apps.users.models import User
from hrrs.apps.resumes.models import Resume

class Workflow(models.Model):
    resume = models.ForeignKey(Resume)
    to_user = models.ForeignKey(User, related_name='workflows_to_user')
    from_user = models.ForeignKey(User, related_name='workflows_from_user')
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    detail = models.TextField(default='', blank=True)
    prevwf = models.ForeignKey('self', null=True, blank=True)