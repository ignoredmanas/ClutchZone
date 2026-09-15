from django.contrib import admin

from .models import Registrations

@admin.register(Registrations)
class RegistrationsAdmin(admin.ModelAdmin):
     list_display = ("team_name", "game", "leader_name", "game_id", "created_at")
     list_filter = ("game",)
     search_fields = ("team_name", "leader_name", "game_id")