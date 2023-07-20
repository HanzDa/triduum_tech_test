from rest_framework import serializers
from API.models import Character
from API.serializers.film_serializer import FilmSerializer


class CharacterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(read_only=True, many=True,
                           fields=('id', 'title', 'release_date', 'producers_count', 'img_url'))

    class Meta:
        model = Character
        fields = '__all__'
        