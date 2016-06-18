# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20160616_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='prize',
        ),
    ]
