from django.urls import path
from .views import HomePageView, ClothingPageView, RandomClothingPageView

urlpatterns = [
    path('', RandomClothingPageView.as_view(), name='random'),
    path('all', HomePageView.as_view(), name='home'),
    path('clothing/<int:pk>', ClothingPageView.as_view(), name='clothing'),
]