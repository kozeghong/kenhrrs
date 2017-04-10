# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import hrrs.apps.resumes.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(default=b'J', max_length=1, choices=[(b'A', b'\xe4\xb8\xad\xe4\xb8\x93/\xe9\xab\x98\xe4\xb8\xad'), (b'B', b'\xe4\xb8\x93\xe7\xa7\x91'), (b'C', b'\xe6\x9c\xac\xe7\xa7\x91'), (b'D', b'\xe7\xa1\x95\xe5\xa3\xab\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f'), (b'E', b'\xe5\x8d\x9a\xe5\xa3\xab\xe7\xa0\x94\xe7\xa9\xb6\xe7\x94\x9f')])),
                ('graduationyear', models.CharField(default=b'2017', max_length=4)),
                ('school', models.CharField(max_length=256)),
                ('faculty', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
                ('projexp', models.TextField(default=b'', blank=True)),
                ('workexp', models.TextField(default=b'', blank=True)),
                ('attachment', models.FileField(upload_to=hrrs.apps.resumes.models.save_path)),
                ('job', models.ForeignKey(to='jobs.Job')),
            ],
        ),
    ]
