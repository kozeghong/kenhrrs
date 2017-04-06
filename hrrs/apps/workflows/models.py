#-*- coding: utf-8
from django.db import models

from hrrs.apps.users.models import User
from hrrs.apps.resumes.models import Resume

class Workflow(models.Model):
    resume = models.ForeignKey(Resume)
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    detail = models.TextField(default='', blank=True)