from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = ('brand', 'price', 'year', 'model', 'ext_color', 'int_color', \
     'transmission', 'contact') 