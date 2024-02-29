from django import forms

from apps.accounts.models import User


class RegisterForm(forms.ModelForm):
    avatar = forms.FileField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password", "avatar")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=56)
    password = forms.CharField(max_length=56)
