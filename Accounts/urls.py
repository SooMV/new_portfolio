from django.urls import path
from Accounts.views import  login_user, signup, logout_user


urlpatterns = [

    path("signup/", signup, name="signup"),
    path('login/', login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]