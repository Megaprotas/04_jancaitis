# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 14:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugfix', '0044_auto_20190506_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='bug',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
