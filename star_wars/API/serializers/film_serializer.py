from rest_framework import serializers

from API.models import Film
from API.serializers.custom_serializer import CustomSerializer
from API.serializers.planet_serializer import PlanetSerializer


class FilmSerializer(CustomSerializer):
    planets = PlanetSerializer(many=True, read_only=True)
    producers_count = serializers.SerializerMethodField('get_producers_count')

    def get_producers_count(self, film):
        return len(film.producers)

    class Meta:
        model = Film
        fields = '__all__'
