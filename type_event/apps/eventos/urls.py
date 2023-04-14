
from django.urls import path

from .views import *

urlpatterns = [
    path('novo_evento/', novo_evento, name="novo_evento"),
    path('gerenciar_evento/', gerenciar_evento, name="gerenciar_evento"),
]
