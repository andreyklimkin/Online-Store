# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_purchases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='number',
        ),
        migrations.AddField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
