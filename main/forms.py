from django import forms
from .models import *

class Apply(forms.ModelForm):
    class Meta:
        model = Applications
        exclude = ('archive','recommended','user','created','test','career', 'career_percent','user')
        labels = {
            'full_name': 'ФИО',
            'education': 'Образование',
            'russian_citizenship' : 'Гражданство РФ',
            'age': 'Возрост',
            'experience': 'Опыт работы',
            'experience_description': 'Опишите опыт работы'
        }
    def save(self, commit=True):
        apply = super(Apply, self).save(commit=False)
        if commit:
            apply.save()
        return apply