from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat, Booking
from .forms import SeatForm, RegisterForm
from datetime import date
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# DRF specific
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer 


def movie_list_view(request):
    movie_list = Movie.objects.all()
    context = {
        "movie_list": movie_list
    }
    return render(request, "movie_list.html", context)

@login_required
def seat_booking_view(request, movie_id):

    movies = Movie.objects.filter(id=movie_id).first()
    seats = Seat.objects.filter(movie=movies, seat_status="Available")
    if request.method == 'POST':
        
        o = request.POST.get('seats')
        print(o)
        print(seats)
        seat_to_edit = seats.filter(seat_number = o).first()
        today = date.today()
        
        print(type(seat_to_edit))
        seat_to_edit.seat_status = 'Booked'
        seat_to_edit.save()
        print(seat_to_edit.seat_status)
        booking = Booking.objects.create(seat = seat_to_edit, user = request.user, movie=movies, booking_date = today)
        print(type(booking.id))
        print("abuot to redirect")
        return redirect('booking_history')
    context = {'seats': seats}
    return render(request, "seat_booking.html", context)

@login_required
def booking_history_view(request):
    # Get all bookings from this user
    user = request.user
    bookings = Booking.objects.filter(user=user)
    print("in booking")
    print(type(bookings))
    context = {'bookings': bookings}
    return render(request, 'booking_history.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("movie_listing")  # Redirect to home page
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})




class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['view_name'] = "Add New Movie"
        return context




class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



