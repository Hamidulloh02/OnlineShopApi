from django.shortcuts import render

# Create your views here.
from .serializers import BrandSerializers,BrandImagesSerializer
from .models import Brand,Brandimages
from rest_framework.generics import ListAPIView,\
                                    RetrieveAPIView,\
                                    CreateAPIView,\
                                    RetrieveUpdateDestroyAPIView,\
                                    RetrieveUpdateAPIView

class BradAPI(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers

class BrandSingleAPI(RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
