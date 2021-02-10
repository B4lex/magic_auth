from django.contrib.auth.backends import BaseBackend, UserModel


class AuthByTokenBackend(BaseBackend):
    def authenticate(self, request, *, token=None, email=None, password=None, **kwargs):
        # authentication with email and password added for login to admin panel
        user = None
        if token:
            try:
                user = UserModel.objects.get(auth_token=token)
            except UserModel.DoesNotExist:
                pass
        elif email and password:
            try:
                user = UserModel.objects.get(email=email)
                if not user.check_password(password):
                    user = None
            except UserModel.DoesNotExist:
                pass
        return user
