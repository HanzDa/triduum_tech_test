from rest_framework import viewsets

from API.serializers import CharacterSerializer
from API.models import Character


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
