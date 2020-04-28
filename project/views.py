from django.shortcuts import render

# Create your views here.
from .models import Clothing, Customer, Donated_Clothing
from django.views.generic import ListView, DetailView
import random
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateDonateForm, CreateRegisterForm, UpdateDonatorForm
from django.urls import reverse
from django.shortcuts import redirect

class HomePageView(ListView):
    model = Clothing
    template_name = 'clothing/home.html'
    context_object_name = 'all_clothing_list'

class DonationPageView(ListView):
    model = Donated_Clothing
    template_name = 'clothing/donated_clothing.html'
    context_object_name = 'all_donation_list'

class ClothingPageView(DetailView):
    model = Clothing
    template_name = 'clothing/clothing.html'
#    context_object_name = 'clothing'
    def get_context_data(self, **kwargs):
        '''Return a dictionary with context data for this template to use'''
        context = super(ClothingPageView, self).get_context_data(**kwargs)
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form
        return context

class CustomerPageView(ListView):
    model = Customer
    template_name = 'clothing/all_donator.html'
    context_object_name = 'all_customer_list'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'clothing/donator.html'
    context_object_name = 'customer'


class RandomClothingPageView(DetailView):
    model = Clothing
    template_name = 'clothing/clothing.html'
    context_object_name = 'clothing'

    def get_object(self):
        all_clothing = Clothing.objects.all()
        r = random.randint(0, len(all_clothing)-1 )
        q = all_clothing[r]
        return q

class CreateDonateView(CreateView):
    form_class = CreateDonateForm
    template_name = "clothing/donate.html"

class CreateRegisterView(CreateView):
    form_class = CreateRegisterForm
    template_name = "clothing/register.html"

class UpdateDonatorView(UpdateView):
    form_class = UpdateDonatorForm
    template_name = "clothing/update_donator.html"
    queryset = Customer.objects.all()

#def add_image(request, pk):
#    '''A custom view function to handle the submission of an image upload.'''
#    clothing = Clothing.objects.get(pk=pk)
#    form = AddImageForm(request.POST or None, request.FILES or None)
#    if form.is_valid():
#        image = form.save(commit=False)
#        image.clothing = clothing
#        image.save()
#    else:
#        print("ErrorL the form was not valid.")

#    url = reverse('clothing', kwargs={'pk':pk})
#    return redirect(url)


