# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfix', '0029_auto_20190504_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_text',
            field=models.CharField(default='Like', max_length=10),
        ),
    ]
