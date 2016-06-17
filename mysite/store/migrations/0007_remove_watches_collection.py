# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20160427_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watches',
            name='collection',
        ),
    ]
