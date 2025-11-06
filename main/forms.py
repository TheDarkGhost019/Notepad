from django import forms
from django.contrib.auth.models import User
from .models import Note


class NoteAddingForm(forms.ModelForm):
    
    addingDate = forms.DateTimeField(widget=forms.DateTimeInput, label="Current date")
    
    class Meta:
        model = Note
        fields = ["title", "addingDate", "dateStart", "dateEnd", "taskIsComplete"]