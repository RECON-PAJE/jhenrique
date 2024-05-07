from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email

class CustomAccountManager(BaseUserManager):
    def create_user(self, matricula, nome, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O e-mail deve ser fornecido")
        email = self.normalize_email(email)
        validate_email(email)

        user = self.model(matricula=matricula, nome=nome, email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, nome, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(matricula, nome, email, password, **extra_fields)
