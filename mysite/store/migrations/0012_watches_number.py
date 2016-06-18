# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_purchases_prize'),
    ]

    operations = [
        migrations.AddField(
            model_name='watches',
            name='number',
            field=models.IntegerField(default=3),
        ),
    ]
