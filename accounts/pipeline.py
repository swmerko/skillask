from django.core.files.base import ContentFile

from requests import request, HTTPError


# public_profile

# def save_location(backend, user, response, details,
#                   is_new=False, *args, **kwargs):
#     if backend.name == 'facebook':
#
#         social = kwargs.get('social')
#         access_token = social.extra_data['access_token']
#         graph = GraphAPI(access_token)
#         #graph.fql('SELECT current_location FROM user WHERE uid=me()')
#
#         user_json = graph.get('me')
#
#         if user_json.get('first_name'):
#             user.first_name = user_json.get('first_name')
#
#         if user_json.get('last_name'):
#             user.last_name = user_json.get('last_name')
#
#         if user_json.get('location'):
#             location_id = user_json.get('location')['id']
#         url = 'http://graph.facebook.com/%s' % location_id
#         try:
#             response = request('GET', url)
#             response.raise_for_status()
#             location_data = response.json()
#             if location_data.get('location') and not (user.geo_lat and user.geo_long):
#                 user.geo_lat = location_data['location'].get('latitude')
#                 user.geo_long = location_data['location'].get('longitude')
#
#             if location_data.get('name') and not user.city:
#                 user.city = location_data.get('name')
#
#         except HTTPError:
#             pass
#
#     user.save()


def save_profile_picture(backend, user, response, details,
                         is_new=False, *args, **kwargs):
    if backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])

        try:
            response = request('GET', url, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            user.profile.image.save('{0}_social.jpg'.format(user.username.encode('utf-8')),
                                    ContentFile(response.content))
            user.profile.save()
