from rest_framework import serializers
from .models import Skill, UserSkill, SupportUserSkill, SkillProposal


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'category', 'slug', 'enabled', 'state')


class CreateSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'slug', 'enabled', 'state')


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill


class SkillProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillProposal


class CreateSkillProposalSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    add_skill_to_user = serializers.BooleanField(default=True)

    class Meta:
        model = SkillProposal
        fields = ('name', 'user', 'add_skill_to_user')


class SupportUserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportUserSkill


class UserSkillExtendedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    skill_id = serializers.IntegerField()
    skill_name = serializers.CharField(max_length=200, source='skill.name')
    user_id = serializers.IntegerField()
    user_email = serializers.EmailField(source='user.email')
    user_profile_image_url = serializers.CharField(source='user.profile.get_image_url')
    user_full_name = serializers.CharField(max_length=200, source='user.get_full_name')
