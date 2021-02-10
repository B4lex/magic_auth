from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class MagicUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    password = models.CharField(max_length=64, default='securepassword123')
    email = models.EmailField(unique=True, error_messages={'unique': 'User with specified email exists.'})
    auth_token = models.CharField(max_length=64, unique=True)
    logins = models.ManyToManyField('magic_auth.LoginActivity')
    has_access = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Magic user')
        verbose_name_plural = _('Magic users')


class LoginActivity(models.Model):
    at = models.DateTimeField(auto_now_add=True)
