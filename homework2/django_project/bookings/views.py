from django.shortcuts import render
from .models import Movie, Seat, Booking
from django.shortcuts import get_object_or_404

# DRF specific
from rest_framework import viewsets
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer 


def movie_list_view(request):
    movie_list = Movie.objects.all()
    context = {
        "movie_list": movie_list
    }
    return render(request, "movie_list.html", context)





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



