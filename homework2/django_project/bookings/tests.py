import pytest
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date

@pytest.mark.django_db
def test_create_movie():
    today = date.today()
    movie = Movie.objects.create(title="test_title", description="testing 1 2 3", release_date = today, duration=2)

    assert movie.title == "test_title"
    assert movie.description == "testing 1 2 3"
    assert movie.release_date == today
    assert movie.duration == 2


@pytest.mark.django_db
def test_seats():
    today = date.today()
    movie = Movie.objects.create(title="test_for_seats", description="testing 1 2", release_date = today, duration=2)
    seat_number = 33
    seat_status = "Available"
    seat = Seat.objects.create(movie=movie, seat_number = seat_number, seat_status=seat_status)

    assert seat.movie == movie
    assert seat.seat_number == 33
    assert seat.seat_status == "Available"
    

@pytest.mark.django_db
def test_booking():
    today = date.today()
    movie = Movie.objects.create(title="test_for_booking", description="testing 1 2 3", release_date = today, duration=2)
    seat = Seat.objects.create(movie=movie, seat_number = 34, seat_status="Booked")
    user = User.objects.create_user(username="testuser", password="password123")

    booking = Booking.objects.create(movie=movie, seat=seat, user=user, booking_date = today)

    assert booking.movie.title == "test_for_booking"
    assert booking.seat.seat_number == 34
    assert booking.user.username == "testuser"
    assert booking.booking_date == today

