# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugfix', '0043_auto_20190506_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_text', models.CharField(max_length=10)),
                ('vote', models.IntegerField(default=0)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_set', to='bugfix.BugTable')),
            ],
        ),
        migrations.RemoveField(
            model_name='vote',
            name='bug',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
