from django import forms

from .models import CesvCurrentMatchs

class CesvCurrentMatchsForm(forms.ModelForm):
    class Meta:
        model = CesvCurrentMatchs
        fields = ('left_team_title', 'left_team_coefficients', 'moneybet_for_left_team', 'left_team_win_percent', 'time_before_match', 'right_team_title', 'right_team_coefficients', 'right_team_win_percent', 'moneybet_for_right_team')
