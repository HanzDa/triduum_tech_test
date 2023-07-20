from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from API.models import Film
from API.serializers.film_serializer import FilmSerializer


class FilmViewSet(viewsets.ViewSet):
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'film_id'

    def list(self, request):
        queryset = Film.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, film_id=None):
        film = get_object_or_404(Film, id=film_id)
        serialized = self.serializer_class(film)
        return Response(serialized.data)
