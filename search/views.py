from django.shortcuts import render, get_object_or_404

from skills.models import Skill, UserSkill


def search(request, skill_id=None):
    skill = get_object_or_404(Skill, pk=skill_id)

    users_skill = UserSkill.objects.filter(skill=skill)

    context = {
        'skill': skill,
        'users_skill': users_skill,
    }

    return render(request, 'search/search.html', context)
