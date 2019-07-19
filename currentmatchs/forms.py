from django import forms

from .models import Cesvcurrentmatchs

class CesvcurrentmatchsForm(forms.ModelForm):
    class Meta:
        model = Cesvcurrentmatchs
        fields = ('Left_team_title', 'Left_team_coefficients', 'Moneybet_for_left_team', 'Left_team_win_percent', 'Time_before_match', 'Right_team_title', 'Right_team_coefficients', 'Right_team_win_percent', 'Moneybet_for_right_team')
