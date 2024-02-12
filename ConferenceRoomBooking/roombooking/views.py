from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

def add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})
