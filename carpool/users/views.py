from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from .serializers import UserSerializer, PlaceSerializer, VehicleSerializer, TripSerializer
from .permissions import IsAuthenticatedUserOrReadOnly, IsOwnerOrReadOnly
from .models import Place, Vehicle, Trip
from .filters import TripFilter


User = get_user_model()

def home(request):
    return HttpResponse("Hello")

class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticatedUserOrReadOnly,
    ]


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    permission_classes = [
        IsOwnerOrReadOnly,
    ]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    permission_classes = [
        IsOwnerOrReadOnly,
        IsAuthenticatedUserOrReadOnly
    ]


    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


class TripViewSet(viewsets.ModelViewSet):
    queryset=Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [
        IsOwnerOrReadOnly, IsAuthenticatedUserOrReadOnly
    ]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FilterViewSet(viewsets.ModelViewSet):
    filterset_class = TripFilter