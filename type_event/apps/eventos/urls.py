
from django.urls import path

from .views import *

urlpatterns = [
    path('novo_evento/', novo_evento, name="novo_evento"),
    path('gerenciar_evento/', gerenciar_evento, name="gerenciar_evento"),
    path('inscrever_evento/<int:id>/',
         inscrever_evento, name="inscrever_evento"),
    path('participantes_evento/<int:id>/',
         participantes_evento, name="participantes_evento"),
    path('gerar_csv/<int:id>/', gerar_csv, name="gerar_csv"),
    path('certificados_evento/<int:id>/',
         certificados_evento, name="certificados_evento"),
    path('gerar_certificado/<int:id>/',
         gerar_certificado, name="gerar_certificado"),
    path('procurar_certificado/<int:id>/',
         procurar_certificado, name="procurar_certificado"),
]
