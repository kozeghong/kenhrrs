# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('summary', models.CharField(max_length=256)),
                ('content', models.TextField(default=b'', blank=True)),
                ('published', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('createdby', models.ForeignKey(related_name='createdby_user', to=settings.AUTH_USER_MODEL)),
                ('modifiedby', models.ForeignKey(related_name='modifiedby_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
