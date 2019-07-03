# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-03 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugfix', '0027_auto_20190503_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_text', models.CharField(max_length=10)),
                ('vote', models.IntegerField(default=0)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugfix.BugTable')),
            ],
        ),
    ]
