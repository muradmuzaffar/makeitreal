
from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name='landing'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
