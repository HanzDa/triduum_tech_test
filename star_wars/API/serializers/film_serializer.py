from rest_framework import serializers

from API.models import Film
from API.serializers import PlanetSerializer, CharacterSerializer


class FilmSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True, read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = '__all__'
        extra_kwargs = {
            'planets': {'write_only': True},
            'characters': {'write_only': True}
        }
