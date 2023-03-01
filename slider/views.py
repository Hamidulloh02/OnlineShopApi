from django.shortcuts import render
from rest_framework.generics import  ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from slider.models import Slider,Position
from .serializers import SliderSerializer,PositionSerializer
# Create your views here.

class PositionAPIView(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class SliderAPIView(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer