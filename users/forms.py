from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    class Meta:
        model=Account
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model=Account
        fields=['username','email']
