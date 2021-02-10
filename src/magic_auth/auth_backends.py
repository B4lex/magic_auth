from django.contrib.auth.backends import UserModel, ModelBackend


class AuthByTokenBackend(ModelBackend):
    def authenticate(self, request, token=None, **kwargs):
        if token:
            try:
                return UserModel.objects.get(auth_token=token)
            except UserModel.DoesNotExist:
                pass
