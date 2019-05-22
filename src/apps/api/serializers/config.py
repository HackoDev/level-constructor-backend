from rest_framework import serializers

from apps.main.models import Config


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ('bool_expression_rules', 'state_expression_rules')
