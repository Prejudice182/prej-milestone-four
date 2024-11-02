from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    '''
    Form class used to create a custom user, inheriting from UserCreationForm
    '''
    email = forms.EmailField(help_text='Required.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    '''
    Form class used to change details about a custom user, inheriting from UserChangeForm
    '''
    email = forms.EmailField(help_text='Required.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
