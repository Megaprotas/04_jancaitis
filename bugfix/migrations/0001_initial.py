# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-22 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_name', models.CharField(max_length=30)),
                ('bug_description', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
