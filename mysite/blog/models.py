from django.conf import settings
from django.db import models
from django.utils import timezone

class Voetbalspeler(models.Model):
    naam = models.CharField(max_length=200)
    actuele_club = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(blank=True, null=True)
    
    def publiceer(self):
        self.datum_laatste_aanpassing = timezone.now()
        self.save()

    def __str__(self):
        return self.naam