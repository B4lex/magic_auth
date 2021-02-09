from django.contrib.auth import get_user_model
from django import forms


class MagicUserSignUpForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)
