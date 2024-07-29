from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.core.validators import validate_email

CARD_NUMBER_VALIDATOR = RegexValidator(regex=r"^\d{10}$")
CPF_VALIDATOR = RegexValidator(regex=r"^\d{11}$")


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password):
        if not email:
            raise ValueError("O e-mail deve ser fornecido")
        email = self.normalize_email(email)
        validate_email(email)
        user = self.model(email=email, nome=nome)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password):
        user = self.create_user(email=email, nome=nome, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = CustomUserManager()


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True, validators=[CPF_VALIDATOR])
    matricula = models.CharField(max_length=6, unique=True)
    numero_cartao = models.CharField(
        max_length=10, unique=True, validators=[CARD_NUMBER_VALIDATOR])


class Relatorio(models.Model):
    solicitante = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='relatorios')
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.solicitante.nome} - {self.timestamp.strftime('%d/%m/%Y %H:%M')}"


class Acesso(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=6)
    numero_cartao = models.CharField(max_length=10)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.nome} - {self.data_hora.strftime('%d/%m/%Y - %H:%M')}"
