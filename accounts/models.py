from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models

from sorl.thumbnail import ImageField

from core.models import GeolocationModel


class UserProfile(GeolocationModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True)
    image = ImageField(upload_to='accounts/images/', null=True)

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None

    def __unicode__(self):
        return '%s Profile' % self.user.get_full_name()

    def skill_ids(self):
        result = []
        for user_skill in self.user.userskill_set.all():
            result.append(user_skill.skill.id)
        return result

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
