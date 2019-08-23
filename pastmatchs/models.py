from django.conf import settings
from django.db import models
from django.contrib.auth.decorators import permission_required
from django.utils import timezone

class CesvPastMatchs(models.Model):
    left_team_title  = models.CharField(max_length=50)
    moneybet_for_left_team = models.IntegerField(default=0)
    score = models.CharField(max_length=50)
    right_team_title = models.CharField(max_length=50)
    moneybet_for_right_team = models.IntegerField(default=0)
    winning_team_match_result = models.CharField(max_length=50)
    hypothesis = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.left_team_title} {self.right_team_title}'
