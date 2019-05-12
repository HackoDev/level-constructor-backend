from rest_framework import serializers

from apps.main.models import Game


class GameSerializer(serializers.ModelSerializer):
    locations = serializers.IntegerField(read_only=True,
                                         source='locations.count')

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'locations')
