# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unab', '0004_auto_20170623_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
