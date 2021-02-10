from django.contrib.auth import get_user_model
from django import forms


class MagicUserSignUpForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.username = self.instance.email.split('@')[0]
        return super().save(commit)

    class Meta:
        model = get_user_model()
        fields = ('email',)
