from django.contrib import admin

# Register your models here.
from .models import Clothing, Color, Customer, Size, Donated_Clothing

admin.site.register(Clothing)
admin.site.register(Color)
admin.site.register(Customer)
admin.site.register(Size)
admin.site.register(Donated_Clothing)