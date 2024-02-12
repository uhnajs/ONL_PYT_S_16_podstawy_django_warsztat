from django import forms
from .models import Room, Reservation
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'projector_availability']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise ValidationError("Data rezerwacji nie może być z przeszłości.")
        return date

