from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Seat

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['seat_number']

    