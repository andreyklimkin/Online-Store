# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20160618_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchases',
            name='total_prize',
            field=models.IntegerField(default=0),
        ),
    ]