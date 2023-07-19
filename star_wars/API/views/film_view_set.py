
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from API.serializers import FilmSerializer
from API.models import Film


class FilmViewSet(viewsets.ModelViewSet):
    
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [AllowAny]
