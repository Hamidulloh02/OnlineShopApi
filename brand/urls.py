from django.urls import path
from .views import BradAPI,BrandSingleAPI

urlpatterns = [
    path('',BradAPI.as_view()),
    path('<int:pk>/',BrandSingleAPI.as_view())
]