# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='createdby',
            field=models.ForeignKey(related_name='jobs_createdby_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='modifiedby',
            field=models.ForeignKey(related_name='jobs_modifiedby_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
