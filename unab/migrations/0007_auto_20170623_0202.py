# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unab', '0006_noticia2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia2',
            name='category',
        ),
        migrations.DeleteModel(
            name='Noticia2',
        ),
    ]
