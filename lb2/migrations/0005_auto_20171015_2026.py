# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lb2', '0004_auto_20171015_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docror',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb2.Docror')),
            ],
        ),
        migrations.AddField(
            model_name='docror',
            name='work_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb2.Hospital'),
        ),
    ]