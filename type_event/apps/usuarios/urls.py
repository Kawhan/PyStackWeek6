
from django.urls import path

from .views import *

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
]
