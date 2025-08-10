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
            product_index = int(id) - 1
            if product_index < 0 or product_index >= len(Product.products):
                return HttpResponseRedirect(reverse('home'))  # Redirect to home
            product = Product.products[product_index]
        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse('home'))  # Redirect if invalid ID

        viewData = {
            "title": product["name"] + " - Online Store",
            "subtitle": product["name"] + " - Product information",
            "product": product
        }
        return render(request, self.template_name, viewData)
