from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["name", "dateJoined", "position", "salary", "contactPerson"]
        widgets = {
            "date_joined": forms.DateInput(attrs={"type": "date"}),
        }

