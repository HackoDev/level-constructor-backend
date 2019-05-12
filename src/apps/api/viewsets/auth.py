from django.contrib.auth import login, logout, update_session_auth_hash
from django.middleware.csrf import rotate_token
from django.utils.translation import ugettext_lazy as _
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.api.serializers import UserSerializer, AuthSerializer


class AuthViewSet(GenericViewSet):

    @action(serializer_class=UserSerializer,
            methods=['post', 'get'],
            url_name='restore-session',
            url_path='restore-session',
            permission_classes=(),
            detail=False)
    def restore_session(self, *args, **kwargs):
        rotate_token(self.request)
        is_authenticated = self.request.user.is_authenticated
        if is_authenticated:
            user = self.request.user
        else:
            user = None
        data = {
            'is_authenticated': is_authenticated,
            'user': self.get_serializer(user).data,
        }
        return Response(data)

    @action(serializer_class=AuthSerializer,
            methods=['post'],
            url_name='login',
            url_path='login',
            permission_classes=(),
            detail=False)
    def login(self, *args, **kwargs):
        serializer: AuthSerializer = self.get_serializer(
            data=self.request.data
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request=self.request, user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    @action(url_name='logout',
            url_path='logout',
            methods=['post'],
            detail=False,
            permission_classes=(),
            serializer_class=AuthSerializer)
    def logout(self, *args, **kwargs):
        logout(self.request)
        return Response({
            'message': _('You successfully logged in')
        })
