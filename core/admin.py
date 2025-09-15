from django.contrib.gis import admin
from .models import PlacesCoordinate , DistrictArea   


admin.site.register(PlacesCoordinate)
admin.site.register(DistrictArea)