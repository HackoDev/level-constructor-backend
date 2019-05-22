from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.api.filters import TransitionFilter
from apps.api.serializers import ConfigSerializer
from apps.main.models import Config


class ConfigViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    serializer_class = ConfigSerializer
    queryset = Config.objects.all()
    filter_class = TransitionFilter

    def get_object(self):
        return Config.get_solo()
