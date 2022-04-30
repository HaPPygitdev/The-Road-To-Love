from .models import Posts
from django.forms import ModelForm, TextInput, Textarea


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }

