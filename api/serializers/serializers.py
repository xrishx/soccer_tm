from rest_framework import serializers
from ..models import Player, Team, Match, Referee, MatchRecord

class TeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['name', 'main_stadium', 'city', 'players']

class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ['name', 'date_of_birth', 'exp']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'date_of_birth', 'start_year', 'shirt_number', 'team']

class MatchSerializer(serializers.ModelSerializer):
    # gives name instead of ID
    host_team_name = serializers.StringRelatedField(source='host_team')
    guest_team_name = serializers.StringRelatedField(source='guest_team')
    referee_name = serializers.StringRelatedField(source='referee')
    class Meta:
        model = Match
        fields = ['match_date', 'host_team', 'host_team_name', 'guest_team', 'guest_team_name', 'referee', 'referee_name']

    def get_final_result(self, obj):
        return obj.final_result

class MatchRecordSerializer(serializers.ModelSerializer):
    match_name = serializers.StringRelatedField(source='match')
    player_name = serializers.StringRelatedField(source='player')
    class Meta:
        model = MatchRecord
        fields = ['match', 'match_name', 'player', 'player_name', 'goals_scored', 'yellow_cards', 'red_cards', 'host_team_score', 'guest_team_score']

