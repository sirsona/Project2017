# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170313_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
