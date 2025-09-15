from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import PlacesCoordinate
from django.contrib.gis.geos import Point

User = get_user_model()


class PlacesCoordinateModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester", password="secret")
        self.place = PlacesCoordinate.objects.create(
            user=self.user,
            name="Cafe A",
            category="cafe",
            location=Point(85.3240, 27.7172),
        )

    def test_string_representation(self):
        """__str__ should return the name."""
        self.assertEqual(str(self.place), "Cafe A")

    def test_defaults_or_constraints(self):
        """Example: category field has expected default or choices."""
        self.assertEqual(self.place.category, "cafe")

    def test_distance_method(self):
        """If you added a custom model method like distance_to()."""
        other = PlacesCoordinate.objects.create(
            user=self.user,
            name="Cafe B",
            category="cafe",
            location=Point(85.3250, 27.7180),
        )
        dist = self.place.location.distance(other.location)
        self.assertGreaterEqual(dist, 0)
