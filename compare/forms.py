from django import forms
from django.forms import ModelForm
from compare.models import UserDetail


class CompareForm(ModelForm):
    class Meta:
        model = UserDetail