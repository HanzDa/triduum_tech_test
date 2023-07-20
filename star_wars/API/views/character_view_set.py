from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from API.models import Character
from API.serializers.character_serializer import CharacterSerializer


class CharacterViewSet(viewsets.ViewSet):
    serializer_class = CharacterSerializer
    permission_classes = [AllowAny]
    lookup_field = 'char_id'

    def list(self, request):
        queryset = Character.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, char_id=None):
        film = get_object_or_404(Character, id=char_id)
        serializer = self.serializer_class(film)
        return Response(serializer.data)
