# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_watches_men'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watches_Women',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'images')),
                ('model', models.CharField(max_length=200)),
                ('firm', models.CharField(max_length=200)),
            ],
        ),
    ]
