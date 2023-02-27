from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from.models import Products,Category
from .serializers import ProductSerializer,CategorySerializers
from .permission import IsAuthorOrReadOnly

#import filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

class ProductsAPIView(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    # permission_classes = IsAuthorOrReadOnly
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductSingleAPIView(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    # permission_classes = IsAuthorOrReadOnly
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class FilterProductAPIView(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['name','category__name']

class CategoryAPIView(ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
