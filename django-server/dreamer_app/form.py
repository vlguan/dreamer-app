from django import forms
from .models import Dreams

class DreamForm(form.ModelForm):
    class Meta:
        model = Dreams
        fields = ['dream_text']