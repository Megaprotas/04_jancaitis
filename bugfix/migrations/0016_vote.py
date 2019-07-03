# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-01 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugfix', '0015_remove_bugtable_upvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_text', models.CharField(max_length=10)),
                ('votes', models.IntegerField(default=0)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugfix.BugTable')),
            ],
        ),
    ]
