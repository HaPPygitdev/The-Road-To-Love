
from .models import User
from django.forms import ModelForm, TextInput, Textarea


class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['description']

        widgets = {
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description',

            })
        }
