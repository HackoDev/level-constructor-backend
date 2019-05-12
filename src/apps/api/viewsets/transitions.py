from rest_framework.viewsets import ModelViewSet

from apps.api.filters import TransitionFilter
from apps.api.serializers import TransitionSerializer
from apps.main.models import Transition


class TransitionViewSet(ModelViewSet):
    serializer_class = TransitionSerializer
    queryset = Transition.objects.all()
    filter_class = TransitionFilter
