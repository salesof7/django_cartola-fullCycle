from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    initial_price = models.FloatField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Match(models.Model):
    team_a = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name="team_a_matches"
    )

    team_b = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name="team_b_matches"
    )

    match_date = models.DateTimeField()
    team_a_gol = models.IntegerField(default=0)
    team_b_gol = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team_a.name} x {self.team_b.name}"


class Action(models.Model):
    match = models.ForeignKey(Match, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)

    minutes = models.IntegerField()

    class Actions(models.TextChoices):
        GOAL = 'goal', 'Goal'
        ASSIST = 'assist', 'Assist'
        YELLOW_CARD = 'yellow card', 'Yellow Card'
        RED_CARD = 'red card', 'Red Card'

    action = models.CharField(max_length=50, choices=Actions.choices)

    def __str__(self):
        return f"{self.minutes}' - {self.player.name} - {self.action}"
