from django.contrib.auth.backends import BaseBackend, UserModel


class AuthByTokenBackend(BaseBackend):
    def authenticate(self, request, token=None, **kwargs):
        try:
            user = UserModel.objects.get(auth_token=token)
        except UserModel.DoesNotExist:
            ...
        else:
            return user
