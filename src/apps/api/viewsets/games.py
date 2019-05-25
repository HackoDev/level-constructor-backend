from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import GameSerializer, GameExtendedSerializer, \
    LocationSerializer, TransitionSerializer
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

    @action(methods=['get'], detail=True)
    def full(self, *args, **kwargs):
        instance = self.get_object()
        transitions = instance.transitions.all()
        locations = instance.locations.all()
        l_serializer = LocationSerializer(locations, many=True)
        t_serializer = TransitionSerializer(transitions, many=True)
        return Response({
            'locations': l_serializer.data,
            'transitions': t_serializer.data
        })
