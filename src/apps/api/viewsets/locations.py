from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.api.filters import LocationFilter
from apps.api.serializers import LocationSerializer, TransitionSerializer
from apps.main.models import Location, Transition


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_class = LocationFilter

    @action(methods=['get'], detail=False)
    def full(self, *args, **kwargs):
        locations = Location.objects.all()
        transitions = Transition.objects.all()
        l_serializer = LocationSerializer(locations, many=True)
        t_serializer = TransitionSerializer(transitions, many=True)
        return Response({
            'locations': l_serializer.data,
            'transitions': t_serializer.data
        })
