# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0002_auto_20150809_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_date', models.DateField(auto_now=True)),
                ('writer', models.CharField(max_length=20)),
                ('review', models.TextField(default=b'no reviews')),
            ],
        ),
        migrations.RemoveField(
            model_name='camera',
            name='review',
        ),
        migrations.AddField(
            model_name='camera',
            name='comment',
            field=models.CharField(default=b'Nice DLSR Camera', max_length=500),
        ),
        migrations.AlterField(
            model_name='camera',
            name='camera_picture',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='camera',
            name='stars',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='review',
            name='camera',
            field=models.ForeignKey(to='cam.Camera'),
        ),
    ]
