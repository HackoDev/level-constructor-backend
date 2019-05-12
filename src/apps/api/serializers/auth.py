from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs['login']
        password = attrs['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({
                'login': _('login or password is invalid')
            })
        return user
