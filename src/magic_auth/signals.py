import base64

from django.contrib.auth.hashers import make_password


def set_auth_token(**kwargs):
    instance = kwargs['instance']
    if kwargs['created']:
        instance.auth_token = base64.urlsafe_b64encode(
            (make_password(instance.email) + hex(instance.id)).encode('utf-8')
        ).decode('utf-8')
        instance.save()
