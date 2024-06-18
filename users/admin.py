from django.contrib import admin
from .models import CustomUser, Aluno, Relatorio, Acesso

admin.site.register(CustomUser)
admin.site.register(Aluno)
admin.site.register(Relatorio)
admin.site.register(Acesso)
