from django.urls import path
from .views import SliderAPIView

urlpatterns = [
    path('',SliderAPIView.as_view())
]
