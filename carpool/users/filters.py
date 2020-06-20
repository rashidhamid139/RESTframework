from django_filters import rest_framework as filters
from .models import Trip

class TripFilter(filters.FilterSet):
    num_seats = filters.NumberFilter(field__name='num_seats', lookup_expr='gte')
    origin = filters.CharFilter(field__name='origin_name', lookup_expr='iexact')
    destination = filters.CharFilter(field_name='destination__name', lookup_expr='iexact')

    class Meta:
        model = Trip
        fields = ['trip_date', 'num_seats', 'origin', 'destination']