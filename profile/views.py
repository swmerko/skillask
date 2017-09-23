from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from skills.models import Skill, UserSkill


@login_required
def add_skills(request):

    users_skill = UserSkill.objects.filter(user=request.user)

    context = {
        'users_skill': users_skill,
    }

    return render(request, 'profile/add_skills.html', context)
