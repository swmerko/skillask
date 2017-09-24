from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect

from skills.models import Skill, UserSkill, SupportUserSkill


@login_required
def support_user_skill(request, user_skill_id=None):
    if user_skill_id:
        user_skill = get_object_or_404(UserSkill, pk=user_skill_id)
        try:
            SupportUserSkill.objects.create(supporter=request.user, user_skill=user_skill)
        except IntegrityError:
            pass

    return redirect(request.META.get('HTTP_REFERER'))

