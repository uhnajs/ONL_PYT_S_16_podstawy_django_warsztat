from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name
