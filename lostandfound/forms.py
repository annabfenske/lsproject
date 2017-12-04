from django import forms
from .models import lostNYUID

class UserForm(forms.ModelForm):
    class Meta:
        model = lostNYUID
        fields = ['net_id']
