# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-02 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfix', '0018_auto_20190502_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='bug',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote',
        ),
        migrations.AddField(
            model_name='bugtable',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bugtable',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
