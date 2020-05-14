from django.db import models
from attraction.models import Attraction
from django.conf import settings

class Plan(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    track = models.ManyToManyField(Attraction)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    final_time = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
