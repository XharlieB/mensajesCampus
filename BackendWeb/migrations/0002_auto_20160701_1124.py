# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='dia',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabajo',
            name='duracionHora',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabajo',
            name='hora',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabajo',
            name='mes',
            field=models.CharField(default=2344, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabajo',
            name='pagoHora',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
