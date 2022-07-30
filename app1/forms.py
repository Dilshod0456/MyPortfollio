from django import forms
from .models import *

class XabarCreatForm(forms.ModelForm):
    class Meta:
        model = Xabarlar
        fields = (
            'fish',
            'tell',
            'email',
            'text',
            )