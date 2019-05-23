from django_filters import rest_framework as filters

from apps.main.models import Location


class LocationFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Location
        fields = ('game', 'type')
