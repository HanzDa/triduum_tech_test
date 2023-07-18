
from django.urls import path
from rest_framework.routers import DefaultRouter
from API.views import PlanetViewSet, FilmViewSet, CharacterViewSet

router = DefaultRouter()

router.register(r'planets', PlanetViewSet, basename='planets')
router.register(r'characters', CharacterViewSet, basename='characters')
router.register(r'films', FilmViewSet, basename='films')

urlpatterns = [
] + router.urls
