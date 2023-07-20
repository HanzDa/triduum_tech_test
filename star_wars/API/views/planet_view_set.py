from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from API.models import Planet
from API.serializers.planet_serializer import PlanetSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    # permission_classes = [AllowAny]
