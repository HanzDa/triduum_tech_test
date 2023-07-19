from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from API.serializers import CharacterSerializer
from API.models import Character


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [AllowAny]
