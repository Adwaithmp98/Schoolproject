from django import forms
from .models import FormEntry

class FormEntryForm(forms.ModelForm):
    class Meta:
        model = FormEntry
        fields = '__all__'
