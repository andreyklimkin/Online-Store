# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_watches_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Watches_Main',
        ),
        migrations.DeleteModel(
            name='Watches_Men',
        ),
        migrations.DeleteModel(
            name='Watches_Women',
        ),
    ]
