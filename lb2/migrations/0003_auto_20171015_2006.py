# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lb2', '0002_propotion_weight'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Propotion',
            new_name='Proportion',
        ),
        migrations.AlterUniqueTogether(
            name='proportion',
            unique_together=set([]),
        ),
    ]