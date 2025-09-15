from .models import  PlacesCoordinate,DistrictArea
from django.contrib.gis.geos import Point

from rest_framework import serializers

class PlacesSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = PlacesCoordinate
        geo_field = "location"
        fields = ["id", "user", "name", "category", "location"]

    def get_user(self, obj):
        return obj.user.username


    def create(self,validated_data):
        location_data=validated_data.pop('location')
        lat,lang=location_data
        loc=Point(float(lang),float(lat))
        return PlacesCoordinate.objects.create(location=loc,**validated_data)
        
        
    
class DistrictAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictArea
        geo_field = "area"
        fields = ["id", "name", "area"]
        
        
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
