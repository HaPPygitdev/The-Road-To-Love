from email.policy import default
from django import forms
from general.models import Poll
from general.models import POLL_TYPES


class PollForm(forms.Form):
    poll_name = forms.CharField(label="Post title", max_length=1000, required=True)
    poll_description = forms.CharField(label="description", max_length=1000, required=True)
    first_var = forms.CharField(label="First option", max_length=100, required=True)
    second_var = forms.CharField(label="Second option", max_length=100, required=True)
    type = forms.ChoiceField(label='Post type', choices=POLL_TYPES, required=True, initial='N_SC')


class SearchByNameForm(forms.Form):
    name_to_find_poll = forms.CharField(label="Name to find poll", max_length=1000, required=True)
