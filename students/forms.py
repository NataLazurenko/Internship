from django import forms
from courses.models import Course
from .models import Student

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        id_user = forms.IntegerField(widget=forms.TextInput)
        age = forms.CharField(widget=forms.TextInput)
        city = forms.CharField(widget=forms.TextInput)
        university = forms.CharField(widget=forms.TextInput)
        direction = forms.CharField(widget=forms.TextInput)
        work_experience = forms.CharField(widget=forms.TextInput)
        internship_direction = forms.CharField(widget=forms.TextInput)