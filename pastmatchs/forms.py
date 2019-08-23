from django import forms

from .models import CesvPastMatchs

class CesvPastMatchsForm(forms.ModelForm):
    class Meta:
        model = CesvPastMatchs
        fields = ('left_team_title', 'moneybet_for_left_team', 'score', 'right_team_title', 'hypothesis')
