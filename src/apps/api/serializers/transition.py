from rest_framework import serializers

from apps.main.models import Transition


class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = (
            'id', 'source', 'target', 'condition', 'state', 'position',
            'weight', 'is_visible', 'meta'
        )
