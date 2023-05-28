from django import forms

from room.models import Room


class SetRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

        id_mentor = forms.IntegerField(widget=forms.TextInput)
        id_student = forms.IntegerField(widget=forms.TextInput)
        text_task = forms.CharField(widget=forms.Textarea)
        task_links = forms.CharField(widget=forms.TextInput)