from django.conf import settings
from django.db import models

from treebeard.mp_tree import MP_Node

from core.models import TimeStampedModel


class Skill(MP_Node, TimeStampedModel):
    name = models.CharField(max_length=64)
    slug = models.SlugField('slug', max_length=64)
    enabled = models.BooleanField(default=False)

    node_order_by = ['name']

    def __unicode__(self):
        return 'Skill: %s' % self.name


class UserSkill(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    skill = models.ForeignKey(Skill)

    def __unicode__(self):
        return "%s_%s" % (self.user.username, self.skill.name)


class SupportUserSkill(TimeStampedModel):
    supporter = models.ForeignKey(settings.AUTH_USER_MODEL)
    user_skill = models.ForeignKey(UserSkill)

    def __unicode__(self):
        return "%s_support_%s_%s" % (
            self.supporter.username, self.user_skill.user.username, self.user_skill.skill.name
        )
