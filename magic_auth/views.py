from django.shortcuts import HttpResponse, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import F

from magic_auth.forms import MagicUserSignUpForm


class MagicUserSignUp(CreateView):
    template_name = 'sign_up.html'
    form_class = MagicUserSignUpForm
    success_url = reverse_lazy('magic_auth:sign_up_success')

    def form_valid(self, form):
        return_value = super().form_valid(form)
        current_site = get_current_site(self.request)
        message = \
            f'''
            Hi, there!\n
            Here is your authentication link:
            http://{current_site}/auth/{self.object.auth_token}\n
            Do not lose!
            '''
        send_mail(
            'Site with a magic authentication',
            message,
            f'noreply@{current_site}',
            (self.object.email,)
        )
        return return_value


class SignUpSuccessView(TemplateView):
    template_name = 'sign_up_success.html'


def magic_user_sign_in(request, token):
    user = authenticate(request, token=token)
    if user:
        user.login_count = F('login_count') + 1
        user.save()
        user.refresh_from_db()
        return render(request, 'page_for_authenticated.html', {'user': user})
    else:
        return HttpResponse('<h1>Invalid auth token.</h1>')
