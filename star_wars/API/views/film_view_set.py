from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from API.models import Film
from API.serializers.film_serializer import FilmSerializer


class FilmViewSet(viewsets.ViewSet):
    serializer_class = FilmSerializer
    permission_classes = [AllowAny]
    lookup_field = 'film_id'

    # def get(self, request, film_id=None):
    #     if film_id:
    #         film = get_object_or_404(Film, id=film_id)
    #         return Response(FilmSerializer(film, many=False).data, status=200)

    def list(self, request):
        queryset = Film.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, film_id=None, **kwargs):
        film = get_object_or_404(Film, id=film_id)
        serializer = self.serializer_class(film)
        return Response(serializer.data)
