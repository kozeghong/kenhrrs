from django.db import models
from hrrs.apps.users.models import User

class Job(models.Model):
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256)
    description = models.TextField(default='', blank=True)
    opened = models.BooleanField(default=False)

    createdby = models.ForeignKey(User, related_name='jobs_createdby_user')
    modifiedby = models.ForeignKey(User, related_name='jobs_modifiedby_user')
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)