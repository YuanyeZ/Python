# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lens',
            name='Camera',
        ),
        migrations.RemoveField(
            model_name='camera',
            name='id',
        ),
        migrations.AddField(
            model_name='camera',
            name='review',
            field=models.TextField(default=b'no review'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='camera_model',
            field=models.CharField(max_length=256, serialize=False, primary_key=True),
        ),
        migrations.DeleteModel(
            name='Lens',
        ),
    ]
