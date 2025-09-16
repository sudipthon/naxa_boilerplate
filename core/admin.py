from django.contrib.gis import admin

from .models import DistrictArea, PlacesCoordinate

admin.site.register(PlacesCoordinate)
admin.site.register(DistrictArea)
