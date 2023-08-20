from . import views
from django.urls import path


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
]
