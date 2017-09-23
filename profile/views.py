from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404

from skills.models import Skill, UserSkill


@login_required
def add_skills(request):

    users_skill = UserSkill.objects.filter(user=request.user)

    context = {
        'users_skill': users_skill,
    }

    return render(request, 'profile/add_skills.html', context)


@login_required
def add_skill(request, skill_id=None):
    if skill_id:
        skill = get_object_or_404(Skill, pk=skill_id)
        try:
            UserSkill.objects.create(user=request.user, skill=skill)
        except IntegrityError:
            pass

    users_skill = UserSkill.objects.filter(user=request.user)

    context = {
        'users_skill': users_skill,
    }

    return render(request, 'profile/add_skills.html', context)
