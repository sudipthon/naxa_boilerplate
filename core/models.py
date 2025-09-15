from django.contrib.gis.db import models
# Create your models here.
from django.contrib.auth.models import User


class PlacesCoordinate(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.PointField()
    category = models.CharField(max_length=50, choices=[
        ("cafe", "Cafe"),
        ("gym", "Gym"),
        ("shop", "Shop"),
    ])

    def __str__(self):
        return self.name
    
class DistrictArea(models.Model):
    name=models.CharField(max_length=100)    
    area=models.PolygonField()       
    
    def __str__(self):
        return self.name    
    