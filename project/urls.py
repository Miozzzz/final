from django.urls import path
from .views import HomePageView, ClothingPageView, RandomClothingPageView, CreateDonateView, CreateRegisterView, CustomerPageView, CustomerDetailView, DonationPageView, UpdateDonatorView

urlpatterns = [
    path('random', RandomClothingPageView.as_view(), name='random'),
    path('home', HomePageView.as_view(), name='home'),
    path('clothing/<int:pk>', ClothingPageView.as_view(), name='clothing'),
    path('donate', CreateDonateView.as_view(), name='donate'),
    path('register', CreateRegisterView.as_view(), name='register'),
    path('all_donator', CustomerPageView.as_view(), name='all_donator'),
    path('all_donator/<int:pk>', CustomerDetailView.as_view(), name='donator'),
    path('donation', DonationPageView.as_view(), name='donation'),
    path('all_donator/<int:pk>/update', UpdateDonatorView.as_view(), name='update_donator'),
]