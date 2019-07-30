from django.conf import settings
from django.db import models
from django.contrib.auth.decorators import permission_required
from django.utils import timezone

class Cesvpastmatchs(models.Model):
    Left_team_title  = models.CharField(max_length=50)
    Moneybet_for_left_team = models.IntegerField(default=0)
    Score = models.CharField(max_length=50)
    Right_team_title = models.CharField(max_length=50)
    Moneybet_for_right_team = models.IntegerField(default=0)
    Winning_team_match_result = models.CharField(max_length=50)
    Hypothesis = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Left_team_title} {self.Right_team_title}'
