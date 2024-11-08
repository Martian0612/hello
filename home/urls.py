from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about',views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('services',views.services, name = 'services'),
    path('examples',views.examples,name = 'examples')
]
