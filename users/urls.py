from django.urls import path
from .views import login_view, registrar_acesso, visualizar_acessos, gerar_relatorio

urlpatterns = [
    path('entrar/', login_view, name='login'),
    path('registrar_acesso/', registrar_acesso, name='registrar_acesso'),
    path('', visualizar_acessos, name='visualizar_acessos'),
    path('gerar_relatorio/', gerar_relatorio, name='gerar_relatorio')
]
