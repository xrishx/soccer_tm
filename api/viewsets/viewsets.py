from rest_framework import viewsets
from ..serializers.serializers import PlayerSerializer, TeamSerializer, MatchSerializer, RefereeSerializer, MatchRecordSerializer
from ..models import Player, Team, Match, Referee, MatchRecord

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

class MatchRecordViewSet(viewsets.ModelViewSet):
    queryset = MatchRecord.objects.all()
    serializer_class = MatchRecordSerializer

