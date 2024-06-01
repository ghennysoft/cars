from django import forms
from .models import CustomUser


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'email', 'phone']
        widgets = {
            'last_name': forms.TextInput(),
            'first_name': forms.TextInput(),
            'email': forms.TextInput(),
            'phone': forms.TextInput(),
        }
