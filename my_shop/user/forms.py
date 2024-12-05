from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import UserModel

class SignIn_User(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput())
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserModel
        fields = ("username","password")

class SignUp_User(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username","first_name","last_name","email","password1","password2")