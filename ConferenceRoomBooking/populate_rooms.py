import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ConferenceRoomBooking.settings')
django.setup()

from roombooking.models import Room

def add_rooms():
    rooms_data = [
        {'name': 'Sala konferencyjna Duża', 'capacity': 50, 'projector_availability': True},
        {'name': 'Sala konferencyjna Średnia', 'capacity': 25, 'projector_availability': False},
        {'name': 'Sala konferencyjna Mała', 'capacity': 10, 'projector_availability': True},
        {'name': 'Sala konferencyjna A', 'capacity': 30, 'projector_availability': False},
        {'name': 'Sala konferencyjna B', 'capacity': 20, 'projector_availability': True},
        {'name': 'Sala konferencyjna C', 'capacity': 15, 'projector_availability': False},
        {'name': 'Sala konferencyjna D', 'capacity': 40, 'projector_availability': True},
        {'name': 'Sala konferencyjna E', 'capacity': 35, 'projector_availability': False},
        {'name': 'Sala konferencyjna F', 'capacity': 45, 'projector_availability': True},
        {'name': 'Sala konferencyjna G', 'capacity': 55, 'projector_availability': False},
    ]

    for room_data in rooms_data:
        room, created = Room.objects.get_or_create(**room_data)
        if created:
            print(f"Dodano salę: {room.name}")
        else:
            print(f"Sala {room.name} już istnieje")

if __name__ == '__main__':
    add_rooms()
