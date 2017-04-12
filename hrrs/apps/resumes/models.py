#-*- coding: utf-8
import os

from django.db import models

from hrrs.apps.users.models import User
from hrrs.apps.jobs.models import Job


def save_path(instance, filename):
    return os.path.join('magazine', instance.name, filename)


class Resume(models.Model):
    job = models.ForeignKey(Job)
    owner = models.ForeignKey(User)

    degree = models.CharField(default='J', max_length=1,
                            choices=(
                                        ('A','中专/高中'),
                                        ('B','专科'),
                                        ('C','本科'),
                                        ('D','硕士研究生'),
                                        ('E','博士研究生'),
                                    )
                            )
    graduationyear = models.CharField(default='2017', max_length=4)
    school = models.CharField(max_length=256)
    faculty = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)

    projexp = models.TextField(default='', blank=True)
    workexp = models.TextField(default='', blank=True)

    attachment = models.FileField(upload_to=save_path)

    date_created = models.DateTimeField(auto_now_add=True)