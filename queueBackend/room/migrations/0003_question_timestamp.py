# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 05:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_question_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 5, 22, 51, 328643, tzinfo=utc), verbose_name='date posted'),
        ),
    ]
