# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 08:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 13, 8, 33, 18, 822526, tzinfo=utc)),
            preserve_default=False,
        ),
    ]