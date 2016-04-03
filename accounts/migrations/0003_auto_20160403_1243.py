# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='geo_lat',
            field=models.DecimalField(null=True, verbose_name=b'latitude', max_digits=13, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='geo_long',
            field=models.DecimalField(null=True, verbose_name=b'longitude', max_digits=13, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='place',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postcode',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'accounts/images/'),
        ),
    ]
