from general.models import Posts, Vote
from django.forms import ModelForm, TextInput, Textarea, Select


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'place', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
            "place": Select(attrs={
                'class': 'form-control'
            }),

        }





