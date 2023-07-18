from rest_framework import viewsets

from API.serializers import PlanetSerializer
from API.models import Planet


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
