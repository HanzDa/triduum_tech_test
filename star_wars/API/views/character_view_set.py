from rest_framework import viewsets

from API.serializers import CharacterSerializer
from API.models import Planet


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = CharacterSerializer
