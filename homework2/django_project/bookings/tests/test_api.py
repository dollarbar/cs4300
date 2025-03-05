import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from bookings.models import Movie, Seat, Booking
from datetime import date

@pytest.mark.django_db
class TestBookingAPI:

    

    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)

    def test_make_movie(self):
        today = date.today()
        Movie.objects.create(title="test_movie_api", description="testing 1 2 3", release_date = today, duration=2)

        response = self.client.get("/api/movies/")

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["title"] == "test_movie_api"

    def test_update_seat(self):
        today = date.today()
        movie = Movie.objects.create(title="test_seat_api", description="testing 1 2 3", release_date = today, duration=2)

        seat = Seat.objects.create(movie=movie, seat_number=35, seat_status="Available")

        data = {"movie":"Updated Movie","seat_number":36, "seat_status": "Booked"}
        response = self.client.put(f"/api/seats/{seat.id}/", data, format="json")

        assert response.status_code == 200
        seat.refresh_from_db()
        assert seat.seat_status == "Booked"
