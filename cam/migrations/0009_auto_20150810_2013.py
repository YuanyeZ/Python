# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0008_auto_20150810_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='camera_picture',
            field=models.ImageField(upload_to=b'/camera_model'),
        ),
    ]
