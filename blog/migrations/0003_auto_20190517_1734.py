# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='date_commented',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='post_commented',
        ),
    ]
