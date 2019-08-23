from django.conf import settings
from django.db import models

class CesvCurrentMatchs(models.Model):
    left_team_title = models.CharField(max_length=50)
    left_team_coefficients = models.CharField(max_length=50)
    moneybet_for_left_team = models.IntegerField(default=0)
    left_team_win_percent = models.CharField(max_length=50)
    time_before_match = models.CharField(max_length=50)
    right_team_title = models.CharField(max_length=50)
    right_team_coefficients = models.CharField(max_length=50)
    moneybet_for_right_team = models.IntegerField(default=0)
    right_team_win_percent = models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.left_team_title} {self.right_team_title}'

