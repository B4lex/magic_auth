from django.apps import AppConfig
from django.db.models.signals import post_save


class MagicAuthConfig(AppConfig):
    name = 'magic_auth'

    def ready(self):
        from .models import MagicUser
        from .signals import set_auth_token
        post_save.connect(set_auth_token, MagicUser)

