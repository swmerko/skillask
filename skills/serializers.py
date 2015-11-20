from rest_framework import serializers

from .models import Skill, UserSkill, SupportUserSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'slug', 'enabled')


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill


class SupportUserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportUserSkill
