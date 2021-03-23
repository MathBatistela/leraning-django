from rest_framework import serializers 
from flights.models import Flight, Airport, Passenger

class FlightModelSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField()
    class Meta:
        model = Flight
        fields = "__all__"
        depth = 1

class AirportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = "__all__"

class PassengerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__" 