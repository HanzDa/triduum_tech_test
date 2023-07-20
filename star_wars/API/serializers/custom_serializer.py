from rest_framework import serializers


class CustomSerializer(serializers.ModelSerializer):
    """ Allow to customize the serialize data to retrieve
    More info https://www.django-rest-framework.org/api-guide/serializers/#example """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


# class UserSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email')
