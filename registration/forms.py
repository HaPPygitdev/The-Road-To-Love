from django import forms
from general.models import PIS_TYPE, Temporary
from django.forms import ModelForm, TextInput


class LoginForm(ModelForm):
    class Meta:
        model = Temporary
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(label="Confirm password", max_length=100)
    first_name = forms.CharField(label="First name", max_length=100)
    second_name = forms.CharField(label="Surname", max_length=100)
    age = forms.CharField(label="Age", max_length=3)
    gender = forms.ChoiceField(label="Your gender: ", choices=PIS_TYPE)
