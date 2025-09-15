
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .serializers import PlacesSerializer, DistrictAreaSerializer,FileUploadSerializer
from .models import PlacesCoordinate as Places, DistrictArea
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.gis.measure import D
from rest_framework.views import APIView, Response
from django.contrib.gis.geos import Point
# from geopy.distance import geodesic
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .tasks import add_districts
from django.core.files.storage import default_storage


class PlacesViewSet(ModelViewSet):

    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Places.objects.all()
        id = self.request.query_params.get("id", None)
        if id:
            queryset = queryset.filter(id=id)
        return queryset

    @action(detail=False, methods=["get"])
    def nearby_place(self, request):
        place_name = request.query_params.get("place_name", None)
        if place_name:
            place_ = Places.objects.filter(name=place_name).first()
            if place_:
                nearby_places = Places.objects.filter(location__distance_lt=(
                    place_.location, D(m=10000))).exclude(id=place_.id)
                serialized = PlacesSerializer(nearby_places, many=True)
                return Response(serialized.data, status=200)
            else:
                return Response({"message": "Place not found"}, status=404)

        return Response({"message": "Place name is required"}, status=400)


class CalculateDistanceAPIView(APIView):
    persmission_classes = [AllowAny]

    def post(self, request):
        place1 = request.data.get("place1", None)
        place2 = request.data.get("place2", None)
        if place1 and place2:
            place1_long, place1_lat = float(
                place1["long"]), float(place1["lat"])
            place2_long, place2_lat = float(
                place2["long"]), float(place2["lat"])

            place1 = Point(place1_long, place1_lat)
            place2 = Point(place2_long, place2_lat)
            distance_km = place1.distance(place2)/1000
            # distance_km = round(geodesic(place1, place2).km, 2)
        return Response({
            "message": f"distance is {distance_km}  km",
            "status": 200
        })


class DistrictAreaViewset(
        CreateModelMixin,
        UpdateModelMixin,
        RetrieveModelMixin,
        DestroyModelMixin,
        ListModelMixin,
        GenericViewSet):

    persmission_classes = [AllowAny]
    serializer_class = DistrictAreaSerializer
    queryset = DistrictArea.objects.all()

    def get_queryset(self):
        queryset = DistrictArea.objects.all()
        pk = self.request.query_params.get("pk", None)
        if pk:
            queryset = queryset.filter(id=pk)
        return queryset

    @action(detail=False, methods=["post"], url_path="check-point")
    def calculate_if_point_in_district(self, request):
        long,lat = request.data.get(
            "long", None)
        lat=request.data.get("lat", None)
        district_name = request.data.get("district_name", None)
        if not all([long, lat, district_name]):
            return Response({
                "message": "long,lat and district_name are required",
                "status": 400
            })

        district = DistrictArea.objects.filter(
            name__icontains=district_name
        ).first()

        point = Point(float(long), float(lat))
        districts = district.area.contains(point)
        if districts:
            return Response({
                "message": f"Point is in {district.name} district",
                "status": 200
            })
        else:
            return Response({
                "message": f"Point is not in {district.name} district",
                "status": 200
            })
            
    @action(detail=False, methods=["post"], url_path="add-districts-file")
    def add_districts_file(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            
            file_name=file.name
            file_path=f"uploads/{file_name}"
            file_saved = default_storage.save(file_path, file)
            add_districts.delay(file_saved)
            print(f"File saved at: {file_saved}")       
  
        return Response({
            "message": "Adding districts in background",
            "status": 200
        })