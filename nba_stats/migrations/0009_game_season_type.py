# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_stats', '0008_auto_20170621_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='season_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
