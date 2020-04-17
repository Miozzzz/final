from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def homePageView(request):

    return HttpResponse('Clothing store')