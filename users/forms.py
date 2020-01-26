from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(help_text='Required.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(help_text='Required.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
