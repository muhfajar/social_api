# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20171115_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventType'),
        ),
    ]