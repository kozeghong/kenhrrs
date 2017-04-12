# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=256)),
                ('detail', models.TextField(default=b'', blank=True)),
                ('from_user', models.ForeignKey(related_name='workflows_from_user', to=settings.AUTH_USER_MODEL)),
                ('prevwf', models.ForeignKey(to='workflows.Workflow')),
                ('resume', models.ForeignKey(to='resumes.Resume')),
                ('to_user', models.ForeignKey(related_name='workflows_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
