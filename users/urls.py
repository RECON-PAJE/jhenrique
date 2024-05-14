from django.urls import path
from .views import registrar_acesso, visualizar_acessos, gerar_relatorio

urlpatterns = [
    path('registrar_acesso/', registrar_acesso, name='registrar_acesso'),
    path('', visualizar_acessos, name='visualizar_acessos'),
    path('gerar_relatorio/', gerar_relatorio, name='gerar_relatorio')
]