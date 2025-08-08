from django.shortcuts import render
from django.http import HttpResponse # new
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
    
from django.views.generic import TemplateView

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
