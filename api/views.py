from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Car
from .serializers import CarSerializer

class CarAPIView(generics.ListAPIView):
  queryset = Car.objects.all()
  serializer_class = CarSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['brand', 'price', 'year', 'model', 'ext_color', 'int_color', 'transmission', 'contact'] 