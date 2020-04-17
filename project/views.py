from django.shortcuts import render

# Create your views here.
from .models import Clothing
from django.views.generic import ListView

class HomePageView(ListView):
    model = Clothing
    template_name = 'clothing/home.html'
    context_object_name = 'all_clothing_list'