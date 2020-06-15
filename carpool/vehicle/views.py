from django.shortcuts import render
from rest_framework import permissions, viewsets
from shared.permissions import IsOwnerOrReadOnly
from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    permission_classes = [
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        