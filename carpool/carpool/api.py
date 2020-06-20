from rest_framework import routers
from users.views import UserViewSet, PlaceViewSet, VehicleViewSet, TripViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('places', PlaceViewSet)
router.register('Vehicles', VehicleViewSet)
router.register('trips', TripViewSet)
