from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

# Create your views here.
# def homePageView(request): # new
#     return HttpResponse('Hello World!') # new

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Contact Us"
        context['subtitle'] = "We’d love to hear from you"
        context['email'] = "info@example.com"
        context['address'] = "123 Main Street, Springfield"
        context['phone'] = "+1 (555) 123-4567"
        return context

from django.views import View
class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV", "price":"$232"},
    {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"$333"},
    {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":"$436"},
    {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":"$123"}
]
class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

from django.urls import reverse
from django.http import HttpResponseRedirect

class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        try:
            product = Product.products[int(id) - 1]
        except (IndexError, ValueError):
            return HttpResponseRedirect('/')

        # Add a numeric version of price (remove $ and convert to int)
        product_numeric_price = int(product["price"].replace("$", ""))
        
        viewData = {
            "title": f"{product['name']} - Online Store",
            "subtitle": f"{product['name']} - Product information",
            "product": product,
            "product_price_number": product_numeric_price
        }
        return render(request, self.template_name, viewData)

from django import forms
from django.shortcuts import render, redirect

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create product",
            "form": form
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Normally save the product to the database
            return redirect('home')  # redirect to route named "home"
        else:
            viewData = {
                "title": "Create product",
                "form": form
            }
            return render(request, self.template_name, viewData)
