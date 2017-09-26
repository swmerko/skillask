import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404

from skills.models import Skill, UserSkill


@login_required
def add_skills(request):
    skill = None
    adviced_skills = []

    users_skill = UserSkill.objects.filter(user=request.user)
    users_skill_ids = request.user.profile.skill_ids()

    if not adviced_skills:
        skills_list_ids = Skill.objects.all().exclude(id__in=users_skill_ids)[:50].values_list('id', flat=True)
        random_skills_ids = random.sample(skills_list_ids, 5)
        adviced_skills = Skill.objects.filter(id__in=random_skills_ids)

    context = {
        'users_skill': users_skill,
        'last_skill_added': skill,
        'adviced_skills': adviced_skills,
    }

    return render(request, 'profile/add_skills.html', context)


@login_required
def add_skill(request, skill_id=None):
    skill = None
    adviced_skills = []

    if skill_id:
        skill = get_object_or_404(Skill, pk=skill_id)
        try:
            UserSkill.objects.create(user=request.user, skill=skill)
        except IntegrityError:
            pass

    users_skill = UserSkill.objects.filter(user=request.user)
    users_skill_ids = request.user.profile.skill_ids()

    if skill_id:
        adviced_skills = skill.get_siblings().exclude(id__in=users_skill_ids).exclude(id=skill.id)

    if not adviced_skills:
        skills_list_ids = Skill.objects.all().exclude(id__in=users_skill_ids)[:50].values_list('id', flat=True)
        random_skills_ids = random.sample(skills_list_ids, 5)
        adviced_skills = Skill.objects.filter(id__in=random_skills_ids)

    context = {
        'users_skill': users_skill,
        'last_skill_added': skill,
        'adviced_skills': adviced_skills,
    }

    return render(request, 'profile/add_skills.html', context)


def public_profile(request, user_id=None):
    user = get_object_or_404(User, pk=user_id)

    users_skill = UserSkill.objects.filter(user=user)

    context = {
        'user': user,
        'users_skill': users_skill,
    }

    return render(request, 'profile/public_profile.html', context)
