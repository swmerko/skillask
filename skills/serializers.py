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


class UserSkillExtendedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    skill_id = serializers.IntegerField()
    skill_name = serializers.CharField(max_length=200, source='skill.name')
    user_id = serializers.IntegerField()
    user_email = serializers.EmailField(source='user.email')
    user_profile_image_url = serializers.CharField(source='user.profile.image.url')
    user_full_name = serializers.CharField(max_length=200, source='user.get_full_name')

