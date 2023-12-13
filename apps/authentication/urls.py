from django.urls import path
from .views import bemvindo, login_view, register_user, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', bemvindo, name="bemvindo"),
    path('login', login_view, name="login"),
    path('register', register_user, name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    path('profile', profile, name="profile"),
]
