from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Room, Reservation
from .forms import RoomForm, ReservationForm
from django.utils import timezone

def add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RoomForm()
    return render(request, 'roombooking/add_room.html', {'form': form})


def room_list(request):
    rooms = Room.objects.all()
    today = timezone.now().date()

    rooms_availability = {}
    for room in rooms:
        reservations = Reservation.objects.filter(room=room, date=today)
        rooms_availability[room.id] = not reservations.exists()

    return render(request, 'roombooking/room_list.html', {
        'rooms': rooms,
        'rooms_availability': rooms_availability,
        'today': today
    })

def modify_room(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # Załóżmy, że 'room_list' to nazwa URL do listy sal
    else:
        form = RoomForm(instance=room)
    return render(request, 'roombooking/modify_room.html', {'form': form})


def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    room.delete()
    return redirect('room_list')


from django.shortcuts import render
from django.utils import timezone
from .models import Room, Reservation


def room_list(request):
    rooms = Room.objects.all()
    today = timezone.now().date()

    # Słownik do przechowywania informacji o zajętości sali
    rooms_availability = {}
    for room in rooms:
        reservations = Reservation.objects.filter(room=room, date=today)
        rooms_availability[room.id] = reservations.exists()

    return render(request, 'roombooking/room_list.html', {
        'rooms': rooms,
        'rooms_availability': rooms_availability,
        'today': today
    })


def modify_room(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            # Tutaj możesz dodać dodatkowe walidacje, jeśli są potrzebne
            if Room.objects.exclude(id=id).filter(name=form.cleaned_data['name']).exists():
                return HttpResponse('Sala o tej nazwie już istnieje.', status=400)
            if form.cleaned_data['capacity'] <= 0:
                return HttpResponse('Pojemność sali musi być większa od zera.', status=400)
            form.save()
            return redirect('room_list')  # Przekieruj do listy sal po zapisaniu zmian
    else:
        form = RoomForm(instance=room)
    return render(request, 'roombooking/modify_room.html', {'form': form, 'room': room})

def reserve_room(request, id):
    room = get_object_or_404(Room, pk=id)
    reservations = room.reservations.all().order_by('date')
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.save()
            return redirect('room_list')
    else:
        form = ReservationForm()
    return render(request, 'roombooking/reserve_room.html', {
        'room': room,
        'form': form,
        'reservations': reservations
    })
def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    reservations = room.reservations.filter(date__gte=timezone.now().date()).order_by('date')
    return render(request, 'roombooking/room_detail.html', {
        'room': room,
        'reservations': reservations
    })

def search_rooms(request):
    query_name = request.GET.get('name', '')
    query_capacity = request.GET.get('capacity', 0)
    query_projector = request.GET.get('projector', False) == 'on'

    rooms = Room.objects.all()
    if query_name:
        rooms = rooms.filter(name__icontains=query_name)
    if query_capacity:
        rooms = rooms.filter(capacity__gte=query_capacity)
    if query_projector:
        rooms = rooms.filter(projector_availability=query_projector)

    return render(request, 'roombooking/room_list.html', {
        'rooms': rooms,
        'search_term': query_name or 'Wszystkie',
        'no_results': not rooms.exists()
    })