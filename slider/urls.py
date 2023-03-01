from django.urls import path
from .views import SliderAPIView,PositionAPIView

urlpatterns = [
    path('',SliderAPIView.as_view()),
    path('positions/',PositionAPIView.as_view())
]
