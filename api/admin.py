from django.contrib import admin
from api.models import Match, Player, Team, MatchRecord, Referee

# Register your models here.
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(MatchRecord)
admin.site.register(Referee)
