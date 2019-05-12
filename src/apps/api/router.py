from rest_framework.routers import DefaultRouter

from apps.api.viewsets import LocationViewSet, TransitionViewSet, GameViewSet, \
    AuthViewSet

router = DefaultRouter()

router.register('auth', AuthViewSet, base_name='auth')
router.register('games', GameViewSet, base_name='games')
router.register('locations', LocationViewSet, base_name='locations')
router.register('transitions', TransitionViewSet, base_name='transitions')
