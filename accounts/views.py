import urllib
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
# Create your views here.
from oauth2_provider.models import AccessToken, Application
from oauth2_provider.settings import oauth2_settings
from oauthlib.oauth2.rfc6749.tokens import random_token_generator


@login_required
def post_social_registration(request):
    expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
    scopes = oauth2_settings.user_settings['SCOPES']
    expires = datetime.now() + timedelta(seconds=expire_seconds)

    application = Application.objects.get(name="SkillaskFrontend")

    access_token = AccessToken.objects.create(
        user=request.user,
        application=application,
        token=random_token_generator(request),
        expires=expires,
        scope=scopes)

    token = access_token.token
    params = {'token': token}
    redirect_url = '%s?' % settings.FRONTEND_BASE_URL + urllib.urlencode(params)

    return redirect(redirect_url)


@login_required
def post_social_login(request):
    expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
    scopes = oauth2_settings.user_settings['SCOPES']
    expires = datetime.now() + timedelta(seconds=expire_seconds)

    application = Application.objects.get(name="SkillaskFrontend")

    access_token = AccessToken.objects.create(
        user=request.user,
        application=application,
        token=random_token_generator(request),
        expires=expires,
        scope=scopes)

    token = access_token.token
    params = {'token': token}
    redirect_url = '%s?' % settings.FRONTEND_BASE_URL + urllib.urlencode(params)

    return redirect(redirect_url)


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)
