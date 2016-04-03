# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0002_auto_20160220_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillProposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
                ('moderator', models.ForeignKey(related_name='moderator_proposal_user', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='state',
            field=models.IntegerField(default=1, choices=[(0, b'pending'), (1, b'approved'), (2, b'rejected')]),
        ),
        migrations.AddField(
            model_name='skillproposal',
            name='skill',
            field=models.ForeignKey(to='skills.Skill'),
        ),
        migrations.AddField(
            model_name='skillproposal',
            name='user',
            field=models.ForeignKey(related_name='skill_proposal_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='skillproposal',
            unique_together=set([('user', 'skill')]),
        ),
    ]
