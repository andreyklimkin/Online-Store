# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(to='store.Brands', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='watches',
            name='prize',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='watches',
            name='brand',
            field=models.ForeignKey(to='store.Brands', null=True),
        ),
        migrations.AddField(
            model_name='watches',
            name='collection',
            field=models.ForeignKey(to='store.Collections', null=True),
        ),
    ]
