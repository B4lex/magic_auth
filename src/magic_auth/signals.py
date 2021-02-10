import base64
import hashlib

from django.conf import settings


def set_auth_token(**kwargs):
    instance = kwargs['instance']
    if kwargs['created']:
        salt = settings.SECRET_KEY
        salted_email_bytes = (instance.email + salt).encode('utf-8')
        instance.auth_token = base64.urlsafe_b64encode(
            (hashlib.sha256(salted_email_bytes).hexdigest() + hex(instance.id)).encode('utf-8')
        ).decode('utf-8')
        instance.save()
