# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190523_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='author',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
