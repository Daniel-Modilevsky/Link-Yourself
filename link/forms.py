from django import forms
from django.forms import ModelForm, TextInput, Select, BooleanField, URLField
from .models import LinkDB, CATALOG_CHOICES
from .models import Profile
import attr
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LinkForm(forms.ModelForm):
    class Meta:
        model = LinkDB
        fields = ['name', 'url', 'catalogChoice', 'isPrivate']

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['catalogChoice'].choices = choices
        self.fields['name'].widget.attrs['placeholder'] = 'Link Name'
        self.fields['name'].widget.attrs['class'] = 'form-control center'
        self.fields['name'].widget.attrs['id'] = 'name'
        self.fields['url'].widget.attrs['placeholder'] = 'link URL'
        self.fields['url'].widget.attrs['class'] = 'form-control center'
        self.fields['url'].widget.attrs['id'] = 'url'
        self.fields['catalogChoice'].widget.attrs['class'] = 'form-control center'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['catalogChoice']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['catalogChoice'].widget.attrs['class'] = 'list-inline center'

