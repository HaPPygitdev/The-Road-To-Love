from django import forms
from general.models import PIS_TYPE


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100)


class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100)
    confirm_password = forms.CharField(label="Confirm password", max_length=100)


class ProfileSignUpForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    second_name = forms.CharField(label="Surname", max_length=100)
    age = forms.DecimalField(label="Age", max_digits=2, decimal_places=0)
    gender = forms.ChoiceField(label="Piska est'?", choices=PIS_TYPE)
