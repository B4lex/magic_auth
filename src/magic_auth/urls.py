from django.urls import path
from django.contrib.auth.views import LogoutView

from magic_auth import views

app_name = 'magic_auth'


urlpatterns = [
    path('', views.MagicUserSignUp.as_view(), name='sign_up'),
    path('sign_up_success', views.SignUpSuccessView.as_view(), name='sign_up_success'),
    path('page_for_authenticated', views.PageForAuthenticatedUsers.as_view(), name='page_for_auth_index'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('<str:token>', views.magic_user_sign_in, name='sign_in'),
]
