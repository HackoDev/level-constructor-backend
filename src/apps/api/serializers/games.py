from rest_framework import serializers

from apps.api.serializers import TransitionSerializer, LocationSerializer
from apps.main.models import Game


class GameSerializer(serializers.ModelSerializer):
    locations = serializers.IntegerField(read_only=True,
                                         source='locations.count')

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'locations', 'initial_state')


class GameExtendedSerializer(serializers.ModelSerializer):
    locations = serializers.IntegerField(read_only=True,
                                         source='locations.count')
    visualization = serializers.SerializerMethodField(read_only=True)

    def get_visualization(self, obj):
        transitions = TransitionSerializer(obj.transitions.all(), many=True)
        locations = LocationSerializer(obj.locations.all(), many=True)
        return {'transitions': transitions.data,
                'locations': locations.data}

    class Meta:
        model = Game
        fields = (
            'id', 'title', 'description', 'locations', 'visualization',
            'initial_state'
        )
