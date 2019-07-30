from django.conf import settings
from django.db import models

class Cesvcurrentmatchs(models.Model):
    Left_team_title = models.CharField(max_length=50)
    Left_team_coefficients = models.CharField(max_length=50)
    Moneybet_for_left_team = models.IntegerField(default=0)
    Left_team_win_percent = models.CharField(max_length=50)
    Time_before_match = models.CharField(max_length=50)
    Right_team_title = models.CharField(max_length=50)
    Right_team_coefficients = models.CharField(max_length=50)
    Moneybet_for_right_team = models.IntegerField(default=0)
    Right_team_win_percent = models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.Left_team_title} {self.Right_team_title}'

