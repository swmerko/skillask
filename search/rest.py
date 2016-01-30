from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from skills.models import Skill, UserSkill
from skills.serializers import UserSkillExtendedSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
def base_search(request):
    """

    :param skill_name:
    :return:
    """
    skill_string = request.REQUEST.get('skill_name')

    if skill_string:

        skill_list = Skill.objects.filter(name__icontains=skill_string)

        skill_as_user_list = UserSkill.objects.filter(skill__in=skill_list)

        serializer = UserSkillExtendedSerializer(skill_as_user_list, many=True)
        result = serializer.data
    else:
        result = []

    return Response(result)
