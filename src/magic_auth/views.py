from django.shortcuts import HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site

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
    if user and user.has_access:
        login(request, user)
        user.logins.create()
        user.save()
        user.refresh_from_db()
        return redirect(reverse_lazy('magic_auth:page_for_auth_index'))
    else:
        return HttpResponse('<h1>Invalid auth token.</h1>')


class PageForAuthenticatedUsers(LoginRequiredMixin, TemplateView):
    template_name = 'authenticated_index.html'
    login_url = reverse_lazy('magic_auth:sign_up')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['login_count'] = self.request.user.logins.count()
        return context_data
