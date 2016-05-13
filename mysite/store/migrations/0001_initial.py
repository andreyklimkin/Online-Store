# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection_Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'images')),
                ('model', models.CharField(max_length=200)),
                ('firm', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Watches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Female')])),
                ('image', models.ImageField(null=True, upload_to=b'images')),
            ],
        ),
        migrations.CreateModel(
            name='Watches_Main',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'images')),
                ('model', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Watches_Men',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'images')),
                ('model', models.CharField(max_length=200)),
                ('firm', models.CharField(max_length=200)),
            ],
        ),
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
