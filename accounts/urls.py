from django.urls import path
from accounts.views import login_view, user_logout, signup_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", signup_view, name="signup"),
]
