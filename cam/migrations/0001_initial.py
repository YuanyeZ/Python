# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camera_model', models.CharField(max_length=256)),
                ('brand', models.CharField(max_length=20)),
                ('camera_picture', models.ImageField(height_field=20, width_field=20, upload_to=b'')),
                ('stars', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lens_model', models.CharField(max_length=256)),
                ('brand', models.CharField(max_length=20)),
                ('lens_picture', models.ImageField(height_field=10, width_field=10, upload_to=b'')),
                ('stars', models.IntegerField(default=0)),
                ('Camera', models.ForeignKey(to='cam.Camera')),
            ],
        ),
    ]
