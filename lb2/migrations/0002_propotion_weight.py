# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lb2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propotion',
            name='weight',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
