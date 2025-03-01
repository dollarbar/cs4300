from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    release_date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title

class Seat(models.Model):
    # many-to-one
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    booking_status = models.TextChoices("BookingStatus", "Booked Available")

    def __str__(self):
        return self.seat_number

class Booking(models.Model):
    # one-to-one for both movie and seat
    # So, I think just one-to-one to seat since seat is a many-to-one to movie
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    booking_date = models.DateField()

    def __str__(self):
        return self.user



    
