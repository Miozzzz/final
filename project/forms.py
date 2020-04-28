from django import forms
from .models import Donated_Clothing, Customer, Image

class CreateDonateForm(forms.ModelForm):
    '''A form to donate a clothes to database'''
    class Meta:
        model = Donated_Clothing
        fields = [ 'text', 'image_url', 'color', 'size','donator', ]

class CreateRegisterForm(forms.ModelForm):
    '''A form to ad a donator to the database'''
    class Meta:
        model = Customer
        fields = ['name', 'age', 'prefered_color', 'email', ]

class UpdateDonatorForm(forms.ModelForm):
    '''A form to update a donator to the database'''
    class Meta:
        model = Customer
        fields = ['name', 'age', 'prefered_color', 'email', ]

class AddImageForm(forms.ModelForm):
    '''A form to collect an image from the user.'''
    class Meta:
        model = Image
        fields = ["image_file",]