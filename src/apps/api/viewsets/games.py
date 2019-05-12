from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import GameSerializer
from apps.main.models import Game


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
