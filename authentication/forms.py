from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput({"placeholder": "Enter your username"}),
    )

    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput({"placeholder": "Enter your email"}),
    )

    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            {
                "class": "password",
                "placeholder": "Enter your password",
            }
        ),
    )

    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            {
                "class": "password",
                "placeholder": "Confirm your password",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=40,
        widget=forms.TextInput({"placeholder": "Enter your username"}),
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            {
                "class": "password",
                "placeholder": "Enter your password",
            }
        ),
    )

    remember_me = forms.Field(widget=forms.CheckboxInput(), required=False)
