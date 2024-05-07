from django.contrib import admin
from .models import CustomUser, UsuarioComum

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'email', 'is_active', 'is_staff']

@admin.register(UsuarioComum)
class UsuarioComumAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'isento', 'creditos', 'numero_cartao']
