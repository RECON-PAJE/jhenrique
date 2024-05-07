from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from .managers import CustomAccountManager

CARD_NUMBER_VALIDATOR = RegexValidator(regex=r"^\d{10}$")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=6, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['nome', 'email']

    def __str__(self):
        return self.nome


class UsuarioComum(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=6, unique=True)
    isento = models.BooleanField(default=False)
    creditos = models.IntegerField(default=0)
    numero_cartao = models.CharField(
        max_length=10, validators=[CARD_NUMBER_VALIDATOR])

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
