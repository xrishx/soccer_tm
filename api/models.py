from django.db import models
from uuid import uuid4

# Create your models here.
class Team(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text='Unique ID for the team')
    name = models.CharField(max_length=100, unique=True, help_text='Name of the team')
    main_stadium = models.CharField(max_length=100, unique=True, help_text='Main stadium of the team')
    city = models.CharField(max_length=100, help_text='City of the stadium')
        
    def __str__(self):
        return self.name
    
class Referee(models.Model):
    referee_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text='Unique ID for the referee')
    name = models.CharField(max_length=100, help_text='Name of the referee')
    date_of_birth = models.DateField(help_text='Date of birth of the referee')
    exp = models.IntegerField(help_text='Number of years of experience of the referee')
    
    def __str__(self):
        return self.name

class Player(models.Model):
    player_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text='Unique ID for the player')
    name = models.CharField(max_length=100, unique=True, help_text='Name of the player')
    date_of_birth = models.DateField(help_text='Date of birth of the player')
    start_year = models.IntegerField(help_text='Starting year of the player')
    shirt_number = models.PositiveIntegerField(help_text='Shirt number of the player')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players', help_text='Team of the player')
    
    def __str__(self):
        return f'{self.name} - {self.team.name}'

class Match(models.Model):
    match_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text='Unique ID for the match')
    match_date = models.DateField(help_text='Date of the match')
    host_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    guest_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, related_name='matches', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.host_team.name} vs {self.guest_team.name}'
    
class MatchRecord(models.Model):
    match = models.ForeignKey(Match, related_name='records', on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name= 'match_records', on_delete=models.CASCADE)
    goals_scored = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Record for {self.player.name} in match {self.match.host_team.name} vs {self.match.guest_team.name}"

    class Meta:
        # Ensures a player has only one record per match
        unique_together = ('match', 'player')

