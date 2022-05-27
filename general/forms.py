from .models import User
from django.forms import ModelForm, Textarea


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


