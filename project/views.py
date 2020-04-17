from django.shortcuts import render

# Create your views here.
from .models import Clothing
from django.views.generic import ListView, DetailView
import random

class HomePageView(ListView):
    model = Clothing
    template_name = 'clothing/home.html'
    context_object_name = 'all_clothing_list'

class ClothingPageView(DetailView):
    model = Clothing
    template_name = 'clothing/clothing.html'
    context_object_name = 'clothing'


class RandomClothingPageView(DetailView):
    model = Clothing
    template_name = 'clothing/clothing.html'
    context_object_name = 'clothing'

    def get_object(self):
        all_clothing = Clothing.objects.all()
        r = random.randint(0, len(all_clothing)-1 )
        q = all_clothing[r]
        return q