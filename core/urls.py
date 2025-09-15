from django.urls import path, include
from core.views import (
    PlacesViewSet,
    DistrictAreaViewset, CalculateDistanceAPIView
)


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'places', PlacesViewSet, 
                basename='places')
router.register(r'districts', DistrictAreaViewset, 
                basename='districts')

urlpatterns = [
    path('', include(router.urls)),
    path("calculate-distance/",CalculateDistanceAPIView.as_view(), name="calculate-distance")

]
