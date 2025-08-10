from django.urls import path
#from .views import homePageView
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, \
ProductShowView, ProductCreateView

urlpatterns = [
    #path("", homePageView,name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    #path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]
