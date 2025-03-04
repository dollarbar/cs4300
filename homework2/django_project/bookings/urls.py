from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet, SeatViewSet, BookingViewSet
from .views import movie_list_view

router = routers.DefaultRouter()
router.register(r'movie-viewset', MovieViewSet)
router.register(r'seat-viewset', SeatViewSet)
router.register(r'booking-viewset', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movie_list/', movie_list_view, name="movie_list"),
]