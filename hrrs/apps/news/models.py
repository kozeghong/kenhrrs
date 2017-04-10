from django.db import models
from hrrs.apps.users.models import User

class Article(models.Model):
    title = models.CharField(max_length=256)
    summary = models.CharField(max_length=256)
    content = models.TextField(default='', blank=True)
    published = models.BooleanField(default=False)

    createdby = models.ForeignKey(User, related_name='news_createdby_user')
    modifiedby = models.ForeignKey(User, related_name='news_modifiedby_user')
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
