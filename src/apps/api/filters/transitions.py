from django_filters import rest_framework as filters

from apps.main.models import Transition


class TransitionFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Transition
        fields = ('source', 'target', 'position', 'weight', 'is_visible')
