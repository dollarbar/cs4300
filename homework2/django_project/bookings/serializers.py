from rest_framework import serializers
from .models import Movie, Seat, Booking





class SeatSerializer(serializers.ModelSerializer):



    movie = serializers.StringRelatedField()
    
    class Meta:
        model = Seat
        fields = ['id','seat_number','movie', 'seat_status']
        read_only_fields = ['id','seat_number','movie']

    def update(self, instance, validated_data):
        """
        Update and return an existing `Seat` instance, given the validated data.
        """

        instance.seat_status = validated_data.get('seat_status', instance.seat_status)

        instance.save()
        return instance



class MovieSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Movie
        seats = SeatSerializer(many=True, required=False)
        fields = '__all__'


    def create(self, validated_data):
        seat_data = validated_data.pop('seat', [])
        movie = Movie.objects.create(**validated_data)
        
        if not seat_data:
            seat_data = [
                {'seat_number':1, 'booking_status':'Available'},
                {'seat_number':2, 'booking_status':'Available'},
                {'seat_number':3, 'booking_status':'Available'},
                {'seat_number':4, 'booking_status':'Available'},
                {'seat_number':5, 'booking_status':'Available'},
                {'seat_number':6, 'booking_status':'Available'},
                {'seat_number':7, 'booking_status':'Available'},
                {'seat_number':8, 'booking_status':'Available'},
                {'seat_number':9, 'booking_status':'Available'},
                {'seat_number':10, 'booking_status':'Available'},
                {'seat_number':11, 'booking_status':'Available'},
                {'seat_number':12, 'booking_status':'Available'},
                {'seat_number':13, 'booking_status':'Available'},
                {'seat_number':14, 'booking_status':'Available'},
                {'seat_number':15, 'booking_status':'Available'},
                {'seat_number':16, 'booking_status':'Available'},
                {'seat_number':17, 'booking_status':'Available'},
                {'seat_number':18, 'booking_status':'Available'},
                {'seat_number':19, 'booking_status':'Available'},
                {'seat_number':20, 'booking_status':'Available'},
            ]

        for seat in seat_data:
            Seat.objects.create(movie=movie, **seat)

        return movie



class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

    
        
