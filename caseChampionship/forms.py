from django import forms
from .models import *

class Championship(forms.ModelForm):
    class Meta:
        model = Championship
        fields = ('file',)
        labels = {
            'file': 'Файл'
        }
    def save(self, commit=True):
        apply = super(Championship, self).save(commit=False)
        if commit:
            apply.save()
        return apply