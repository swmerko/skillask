from core.models import TimeStampedModel
from django.conf import settings
from django.db import models
from treebeard.mp_tree import MP_Node

STATES = (
    (0, 'pending'),
    (1, 'approved'),
    (2, 'rejected')
)


CATEGORY = (
    (0, 'unset'),
    (1, 'brain'),
    (2, 'sport'),
    (3, 'hands'),
    (4, 'art'),
)


class Skill(MP_Node, TimeStampedModel):
    name = models.CharField(max_length=64)
    slug = models.SlugField('slug', max_length=64)
    enabled = models.BooleanField(default=True)
    state = models.IntegerField(choices=STATES, default=1)
    category = models.IntegerField(choices=CATEGORY, default=0)

    node_order_by = ['name']

    def __unicode__(self):
        return 'Skill: %s' % self.name


class SkillProposal(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='skill_proposal_user')
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='moderator_proposal_user')
    skill = models.ForeignKey(Skill)
    closed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'skill',)

    def __unicode__(self):
        return "%s_propose_%s" % (self.user.username, self.skill.name)


class UserSkill(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    skill = models.ForeignKey(Skill)

    class Meta:
        unique_together = ('user', 'skill',)

    def __unicode__(self):
        return "%s_%s" % (self.user.username, self.skill.name)


class SupportUserSkill(TimeStampedModel):
    supporter = models.ForeignKey(settings.AUTH_USER_MODEL)
    user_skill = models.ForeignKey(UserSkill)

    class Meta:
        unique_together = ('supporter', 'user_skill',)

    def __unicode__(self):
        return "%s_support_%s_%s" % (
            self.supporter.username, self.user_skill.user.username, self.user_skill.skill.name
        )
