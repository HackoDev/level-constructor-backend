from rest_framework import serializers

from apps.main.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id', 'name', 'description', 'is_start', 'is_finish', 'meta',
            'game'
        )
