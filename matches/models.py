from django.db import models

class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    match_time = models.DateTimeField()  # Date and time together
    venue = models.CharField(max_length=200)
    watch = models.CharField(max_length=100, default='Not available')

    def __str__(self):
        return f"{self.team1} vs {self.team2} at {self.venue}"
