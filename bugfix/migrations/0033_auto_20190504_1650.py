# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugfix', '0032_auto_20190504_1642'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='preference',
            name='bug',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]
