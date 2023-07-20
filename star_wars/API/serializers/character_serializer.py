from rest_framework import serializers
from API.models import Character
from API.serializers import FilmSerializer


class CharacterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(read_only=True, many=True,
                           fields=('id', 'title', 'release_date', 'producers_count'))

    class Meta:
        model = Character
        fields = '__all__'
        