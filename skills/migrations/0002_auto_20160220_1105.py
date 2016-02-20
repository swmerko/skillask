# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='supportuserskill',
            unique_together=set([('supporter', 'user_skill')]),
        ),
        migrations.AlterUniqueTogether(
            name='userskill',
            unique_together=set([('user', 'skill')]),
        ),
    ]
