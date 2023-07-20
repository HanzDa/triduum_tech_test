
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from API.views import PlanetViewSet, FilmViewSet, CharacterViewSet

router = DefaultRouter()

router.register(r'planets', PlanetViewSet, basename='planets')
router.register(r'characters', CharacterViewSet, basename='characters')
router.register(r'films', FilmViewSet, basename='films')

urlpatterns = [
    # re_path(r'^films/(?:(?P<film_id>\d+)/)?$', FilmViewSet.as_view(), name='film'),
] + router.urls
