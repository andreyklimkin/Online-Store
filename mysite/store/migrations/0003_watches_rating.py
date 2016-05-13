# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160425_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='watches',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
