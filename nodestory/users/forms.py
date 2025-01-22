from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "password1", "password2")


class UpdateMailForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["email"]


class UpdateUsernameForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username"]
