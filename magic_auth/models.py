import base64

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver


class MagicUser(AbstractUser):
    password = None
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, error_messages={'unique': 'User with specified email exists.'})
    auth_token = models.CharField(max_length=64, unique=True)
    login_count = models.PositiveSmallIntegerField(default=0)
    has_access = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


@receiver(models.signals.post_save, sender=MagicUser)
def set_auth_token(**kwargs):
    instance = kwargs['instance']
    if not instance.auth_token:
        instance.auth_token = base64.urlsafe_b64encode(
            (make_password(instance.email) + hex(instance.id)).encode('utf-8')
        ).decode('utf-8')
        instance.save()
