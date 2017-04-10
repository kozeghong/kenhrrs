# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='createdby',
            field=models.ForeignKey(related_name='news_createdby_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='modifiedby',
            field=models.ForeignKey(related_name='news_modifiedby_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
