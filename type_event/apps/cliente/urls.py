from django.urls import path

from .views import *

urlpatterns = [
    path('meus_certificados/', meus_certificados, name="meus_certificados"),
]
