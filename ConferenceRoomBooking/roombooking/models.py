from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField(default=False)
    # Dodatkowe pola dla modelu Room, jeśli są potrzebne

class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('date', 'room')
        ordering = ['date']

    def __str__(self):
        return f"Rezerwacja {self.room.name} na dzień {self.date}"