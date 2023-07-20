from rest_framework import serializers


class CustomSerializer(serializers.ModelSerializer):
    """ Allow to customize the serialize data to retrieve
    More info https://www.django-rest-framework.org/api-guide/serializers/#example """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' or 'exclude' kwargs up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        super().__init__(*args, **kwargs)

        self._only_fields(fields)
        self._exclude_fields(exclude)

    def _only_fields(self, fields):
        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def _exclude_fields(self, exclude):
        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name)
