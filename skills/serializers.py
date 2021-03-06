from rest_framework import serializers
from .models import Skill, UserSkill, SupportUserSkill, SkillProposal


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'category', 'slug', 'enabled', 'state', 'category')


class CreateSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'slug', 'enabled', 'state')


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill


class UserSkillExtendedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    skill = serializers.IntegerField(source='skill_id')
    skill_category = serializers.IntegerField(source='skill.category')
    skill_name = serializers.CharField(max_length=200, source='skill.name')
    user = serializers.IntegerField(source='user_id')
    user_email = serializers.EmailField(source='user.email')
    user_profile_image_url = serializers.CharField(source='user.profile.get_image_url')
    user_full_name = serializers.CharField(max_length=200, source='user.get_full_name')


class UserSkillExtendedWithSupportersSerializer(UserSkillExtendedSerializer):
    supporters = serializers.ListField(required=False)


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
