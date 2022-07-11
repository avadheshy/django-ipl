from django.db import models

# Create your models here.


class Matches(models.Model):
    season = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    toss_winner = models.CharField(max_length=200)
    toss_decision = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=200)
    win_by_runs = models.PositiveIntegerField()
    win_by_wickets = models.PositiveIntegerField()
    player_of_match = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    umpire1 = models.CharField(max_length=200)
    umpire2 = models.CharField(max_length=200)


class Deliveries(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE, null=True)
    inning = models.PositiveIntegerField()
    batting_team = models.CharField(max_length=200, null=True)
    bowling_team = models.CharField(max_length=200, null=True)
    over = models.PositiveIntegerField()
    ball = models.PositiveIntegerField()
    batsman = models.CharField(max_length=200, null=True)
    non_striker = models.CharField(max_length=200, null=True)
    bowler = models.CharField(max_length=200, null=True)
    is_super_over = models.PositiveIntegerField()
    wide_runs = models.PositiveIntegerField()
    bye_runs = models.PositiveIntegerField()
    legbye_runs = models.PositiveIntegerField()
    noball_runs = models.PositiveIntegerField()
    penalty_runs = models.PositiveIntegerField()
    batsman_runs = models.PositiveIntegerField()
    extra_runs = models.PositiveIntegerField()
    total_runs = models.PositiveIntegerField()
    player_dismissed = models.CharField(max_length=100, null=True)
    dismissal_kind = models.CharField(max_length=100, null=True)
    fielder = models.CharField(max_length=100, null=True)
