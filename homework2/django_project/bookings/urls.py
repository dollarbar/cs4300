from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet, SeatViewSet, BookingViewSet
from .views import movie_list_view, seat_booking_view, booking_history_view, register

router = routers.DefaultRouter()
router.register(r'movie-viewset', MovieViewSet)
router.register(r'seat-viewset', SeatViewSet)
router.register(r'booking-viewset', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name="register"),
    path('movie_list/', movie_list_view, name="movie_list"),
    path('seat_booking/<int:movie_id>/', seat_booking_view, name="seat_booking"),
    path('booking_history/', booking_history_view, name="booking_history"), 
]