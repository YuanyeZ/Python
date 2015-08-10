# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0006_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='camera_model',
            field=models.CharField(max_length=255, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='camera',
            name='comment',
            field=models.CharField(default=b'Nice DLSR Camera', max_length=255),
        ),
    ]
