from django import forms
from .models import SocieteAviation


class VoyageForm(forms.ModelForm):
    class Meta:
        model = SocieteAviation
        fields = ['name', 'image']
        