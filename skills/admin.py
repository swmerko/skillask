from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Skill, UserSkill, SupportUserSkill


class SkillAdmin(TreeAdmin):
    prepopulated_fields = {'slug': ('name',)}
    form = movenodeform_factory(Skill)


admin.site.register(Skill, SkillAdmin)
admin.site.register(UserSkill)
admin.site.register(SupportUserSkill)
