# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20160403_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.IntegerField(default=0, choices=[(0, b'unset'), (1, b'brain'), (2, b'sport'), (3, b'hands'), (4, b'art')]),
        ),
        migrations.AlterField(
            model_name='skill',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
