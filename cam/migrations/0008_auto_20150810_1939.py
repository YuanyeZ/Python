# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0007_auto_20150810_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='camera_picture',
            field=models.ImageField(upload_to=b'../../static/cam/images/camera_model'),
        ),
    ]
