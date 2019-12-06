from django.urls import path
from .views import CarAPIView

urlpatterns = [
  path('', CarAPIView.as_view())
]