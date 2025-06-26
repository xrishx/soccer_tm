from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.viewsets.viewsets import PlayerViewSet, TeamViewSet, MatchViewSet, RefereeViewSet, MatchRecordViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'referees', RefereeViewSet)
router.register(r'match_records', MatchRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]