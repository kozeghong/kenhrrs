# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='prevwf',
            field=models.ForeignKey(blank=True, to='workflows.Workflow', null=True),
        ),
    ]
