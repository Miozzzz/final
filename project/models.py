from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    '''a model that stores the customer database'''
    name = models.TextField(blank=False)
    age = models.TextField(blank=True)
    email = models.TextField(blank=True)
    prefered_color = models.ForeignKey('Color', on_delete="None")

    def __str__(self):
        '''string representation'''
        return self.name

    def get_absolute_url(self):
        '''direction to all donator page'''
        return '/clothing/all_donator/%i' % self.pk

class Clothing(models.Model):
    '''a model that stores the clothing database'''
    text = models.TextField(blank=True)
    size = models.ForeignKey('Size', on_delete="None")
    image_url = models.URLField(blank=True)
    price = models.TextField(blank=True)
    buyer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete="None")
    def __str__(self):
        '''string representation'''
        return self.text

class Donated_Clothing(models.Model):
    '''a model that stores the donated clothing database'''
    text = models.TextField(blank=True)
    size = models.ForeignKey('Size', on_delete="None")
    image_url = models.URLField(blank=True)
    color = models.ForeignKey('Color', on_delete="None")
    donator = models.ForeignKey('Customer', on_delete="None")
    def __str__(self):
        '''string representation'''
        return self.text   
    
    def get_absolute_url(self):
        '''direction to donation page'''
        return '/clothing/donation'

class Image(models.Model):
    '''Represent an image'''
    image_file = models.ImageField(blank=True)
    clothing = models.ForeignKey('Clothing', on_delete=models.CASCADE)

class Size(models.Model):
    '''a model that stores the size database'''
    text = models.TextField(blank=True)
    def __str__(self):
        '''string representation'''
        return self.text


class Color(models.Model):
    '''a model that stores the color database'''
    text = models.TextField(blank=True)
    def __str__(self):
        '''string representation'''
        return self.text