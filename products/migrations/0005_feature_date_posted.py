# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190426_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
