# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_watches_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watches',
            name='brand',
        ),
        migrations.AddField(
            model_name='watches',
            name='collection',
            field=models.ForeignKey(to='store.Collections', null=True),
        ),
    ]
