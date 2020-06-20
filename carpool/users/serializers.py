from datetime import date
from rest_framework import serializers
from dateutil.relativedelta import relativedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Place, Vehicle, Trip

class UserSerializer(serializers.HyperlinkedModelSerializer):

    def validate_birth_date(self, value):
        if value:
            if value > date.today():
                raise serializers.ValidationError('Birth Date cannot be in the future')
            age = relativedelta(date.today(), value).years
            if age < 18:
                raise serializers.ValidationError('User Should be 18 years or older')
        return value

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'gender', 'birth_date', 'url', 'profile_pic']


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name']

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields  = ["id", "url", "make", "model", "reg_number", "image"]



class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(
            UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(user=request.user)


class TripSerializer(serializers.HyperlinkedModelSerializer):
    origin_id = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        source='origin',
        write_only=True
    )

    origin = PlaceSerializer(read_only=True)

    destination_id = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        source='destination',
        write_only=True

    )
    destination = PlaceSerializer(read_only=True)

    vehicle_id = UserFilteredPrimaryKeyRelatedField(
        queryset=Vehicle.objects,
        source='vehicle',
        write_only=True
    )

    vehicle = VehicleSerializer(read_only=True)

    driver = UserSerializer(source='user', read_only=True)

    def validate_trip_date(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                'Trip date cannot be in the past')
        return value

    def validate(self, data):
        if data['origin'] == data['destination']:
            raise serializers.ValidationError(
                'Origin and destination cannot be the same')

        return data

    class Meta:
        model = Trip
        fields = [
            'id',
            'url',
            'trip_date',
            'num_seats',
            'origin_id',
            'origin',
            'destination_id',
            'destination',
            'vehicle_id',
            'vehicle',
            'driver',
        ]