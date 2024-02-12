from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),  # Lista wszystkich sal
    path('new/', views.add_room, name='add_room'),  # Dodawanie nowej sali
    path('modify/<int:id>/', views.modify_room, name='modify_room'),  # Modyfikacja sali
    path('delete/<int:id>/', views.delete_room, name='delete_room'),  # Usuwanie sali
    path('<int:id>/', views.room_detail, name='room_detail'),  # Szczegółowy widok sali
    path('reserve/<int:id>/', views.reserve_room, name='reserve_room'),  # Rezerwacja sali
    path('search/', views.search_rooms, name='search_rooms'),
]
