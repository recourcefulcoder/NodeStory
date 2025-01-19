from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

app_name = "users"

settings_block = [
    path("stories/", views.review, name="review"),
    path(
        "change_password/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change"
    ),
    path("change_username/", views.review, name="username_change"),
    path("change_email/", views.review, name="email_change"),
]

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("settings/", include(settings_block)),
]
