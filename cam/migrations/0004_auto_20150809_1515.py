# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0003_auto_20150809_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='writer',
            field=models.CharField(default=b'Ted', max_length=20),
        ),
    ]
