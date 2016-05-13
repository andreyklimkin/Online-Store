# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20160427_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='user_id',
            new_name='user_name',
        ),
    ]
