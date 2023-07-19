from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from API.serializers import PlanetSerializer
from API.models import Planet


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    # permission_classes = [AllowAny]
