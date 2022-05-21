from django import forms
from general.models import Temporary
from django.forms import ModelForm, TextInput, Textarea


class LoginForm(ModelForm):
    class Meta:
        model = Temporary
        fields = ['username', 'password', 'coordinate']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "coordinate": Textarea(attrs={
                'class': 'silent-coords',
                'placeholder': 'coordinate',
                'id': 'demo',

            }),
        }


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)


class SignUpForm(ModelForm):
    class Meta:
        model = Temporary
        fields = ['username', 'password', 'confirm_password', 'first_name', 'second_name', 'age', 'gender', 'coordinate']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "confirm_password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Second name'
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age'
            }),
            "coordinate": Textarea(attrs={
                'class': 'silent-coords',
                'placeholder': 'coordinate',
                'id': 'demo'
            }),
        }
