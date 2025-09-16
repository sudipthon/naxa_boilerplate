from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views import CalculateDistanceAPIView, DistrictAreaViewset, PlacesViewSet

router = DefaultRouter()
router.register(r"places", PlacesViewSet, basename="places")
router.register(r"districts", DistrictAreaViewset, basename="districts")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "calculate-distance/",
        CalculateDistanceAPIView.as_view(),
        name="calculate-distance",
    ),
]
