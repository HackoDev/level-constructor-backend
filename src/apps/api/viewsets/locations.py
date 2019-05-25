from rest_framework.viewsets import ModelViewSet

from apps.api.filters import LocationFilter
from apps.api.serializers import LocationSerializer
from apps.main.models import Location


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_class = LocationFilter
