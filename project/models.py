from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    name = models.TextField(blank=False)
    age = models.TextField(blank=True)
    email = models.TextField(blank=True)
    prefered_color = models.ForeignKey('Color', on_delete="None")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/clothing/all_donator/%i' % self.pk

class Clothing(models.Model):
    text = models.TextField(blank=True)
    size = models.ForeignKey('Size', on_delete="None")
    image_url = models.URLField(blank=True)
    price = models.TextField(blank=True)
    buyer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete="None")
    def __str__(self):
        return self.text

class Donated_Clothing(models.Model):
    text = models.TextField(blank=True)
    size = models.ForeignKey('Size', on_delete="None")
    image_url = models.URLField(blank=True)
    color = models.ForeignKey('Color', on_delete="None")
    donator = models.ForeignKey('Customer', on_delete="None")
    def __str__(self):
        return self.text   
    
    def get_absolute_url(self):
        return '/clothing/donation'

class Image(models.Model):
    '''Represent an image'''
    image_file = models.ImageField(blank=True)
    clothing = models.ForeignKey('Clothing', on_delete=models.CASCADE)

class Size(models.Model):
    text = models.TextField(blank=True)
    def __str__(self):
        return self.text


class Color(models.Model):
    text = models.TextField(blank=True)
    def __str__(self):
        return self.text