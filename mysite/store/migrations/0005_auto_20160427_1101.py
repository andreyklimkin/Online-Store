# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_auto_20160425_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cart_items',
            name='cart',
            field=models.ForeignKey(to='store.Carts', null=True),
        ),
        migrations.AddField(
            model_name='cart_items',
            name='item',
            field=models.ForeignKey(to='store.Watches', null=True),
        ),
    ]
