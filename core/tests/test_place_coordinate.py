from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from core.models import PlacesCoordinate
from django.contrib.gis.geos import Point


class PlacesCoordinateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.base_url = "/api/v1"

    def test_create_place_coordinate(self):
        url = f"{self.base_url}/core/places/"
        data={
            "name": "Test Place",
            "category": "cafe",
            "location": ("89.300140", "27.700769")  # Longitude, Latitude
            }
        response=self.client.post(url, data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data["name"], "Test Place")
    
    def test_nearby_place(self):
        
        url=f"{self.base_url}/core/places/nearby_place/"
        place1=PlacesCoordinate.objects.create(
            user=self.user,
            name="Place 1",
            category="cafe",
            location=Point(89.300140, 27.700769) # Kathmandu
        )
        place2=PlacesCoordinate.objects.create(
            user=self.user,
            name="Place 2",
            category="gym",
            location=Point(85.3240, 27.7172) # Pokhara
        )
        place3=PlacesCoordinate.objects.create(
            user=self.user,
            name="Place 3",
            category="shop",
            location=Point(88.2093, 26.9226) # Birat
        ) 
        Place4=PlacesCoordinate.objects.create(
            user=self.user,
            name="Place 4",
            category="shop",
            location=Point(89.3300, 27.7100) # Nearby Kathmandu
        )
        response=self.client.get(url, {'place_name': 'Place 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 0)  # No nearby places within 10 km
        
        

class CalculateDistanceAPITestCase(APITestCase):
    def setUp(self):
        self.base_url = "/api/v1"

    def test_calculate_distance(self):
        url = f"{self.base_url}/core/calculate-distance/"
        place1={
            "long": "89.300140",
            "lat": "27.700769"
        }
        place2={
            "long": "85.3240",
            "lat": "27.7172"
        }
        data={
            "place1": place1,
            "place2": place2
        }
        response = self.client.post(url, data, format="json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIn("distance is", response.data["message"])