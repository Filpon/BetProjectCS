from django import forms

from .models import Cesvpastmatchs

class CesvpastmatchsForm(forms.ModelForm):
    class Meta:
        model = Cesvpastmatchs
        fields = ('Left_team_title', 'Moneybet_for_left_team', 'Score', 'Right_team_title', 'Hypothesis')
