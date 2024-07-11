from django.db import models


class ReconhecimentoFacial(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    reconheceu = models.BooleanField(default=False)
    registro_acesso = models.CharField(max_length=100)

    def __str__(self):
        return f"Reconhecimento em {
            self.date} - {'Sucesso' if self.reconheceu else 'Falhou'}"
