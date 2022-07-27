from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
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