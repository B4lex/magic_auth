from django.urls import path
from magic_auth import views


app_name = 'magic_auth'


urlpatterns = [
    path('', views.MagicUserSignUp.as_view(), name='sign_up'),
    path('sign_up_success', views.SignUpSuccessView.as_view(), name='sign_up_success'),
    path('<str:token>', views.magic_user_sign_in, name='sign_in'),
]
