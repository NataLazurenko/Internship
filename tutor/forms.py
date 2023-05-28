from django import forms

from tutor.models import SetMentorToStudent


class SetMentorToStudentForm(forms.ModelForm):
    class Meta:
        model = SetMentorToStudent
        fields = "__all__"

        id_mentor = forms.IntegerField(widget=forms.TextInput)
        id_student = forms.IntegerField(widget=forms.TextInput)
        id_tutor = forms.IntegerField(widget=forms.TextInput)