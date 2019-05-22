from rest_framework.routers import DefaultRouter

from apps.api import viewsets

router = DefaultRouter()

router.register('auth', viewsets.AuthViewSet, base_name='auth')
router.register('config', viewsets.ConfigViewSet, base_name='config')
router.register('games', viewsets.GameViewSet, base_name='games')
router.register('locations', viewsets.LocationViewSet, base_name='locations')
router.register('transitions', viewsets.TransitionViewSet, base_name='transitions')
