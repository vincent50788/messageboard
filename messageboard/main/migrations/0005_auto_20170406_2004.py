# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170406_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]