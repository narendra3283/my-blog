# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 17:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='testfield',
            field=models.IntegerField(default=124),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 27, 22, 47, 22, 642000)),
        ),
    ]
