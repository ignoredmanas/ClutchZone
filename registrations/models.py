from django.db import models

class Registrations(models.Model):
    GAME_CHOICES = [
        ("valorant","Valorant"),
        ("bgmi","BGMI"),
        ("free-fire","Free Fire"),
    ]
    team_name = models.CharField(max_length=1000)
    game = models.CharField(max_length=20,choices=GAME_CHOICES)
    leader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} - {self.game}"
    
