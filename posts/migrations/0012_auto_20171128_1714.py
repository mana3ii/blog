# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-28 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
