from rest_framework import serializers

from apps.main.models import Transition


class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = (
            'id', 'source', 'target', 'position',
            'weight', 'is_visible', 'meta',
            'condition', 'state',
            'condition_rules', 'state_rules'
        )
