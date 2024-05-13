from django.urls import path
from .views import registrar_acesso, visualizar_acessos

urlpatterns = [
    path('registrar_acesso/', registrar_acesso, name='registrar_acesso'),
    path('', visualizar_acessos, name='visualizar_acessos'),
]