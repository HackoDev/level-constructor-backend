from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import GameSerializer, GameExtendedSerializer
from apps.main.models import Game


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    @action(detail=True, methods=['get'],
            serializer_class=GameExtendedSerializer)
    def visualization(self, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)
