# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-26 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20180223_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
        migrations.AddField(
            model_name='posts',
            name='banana',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to='login_app.Users'),
            preserve_default=False,
        ),
    ]
