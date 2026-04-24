from django.db import models
from django.conf import settings
import re
from django.core.exceptions import ValidationError


def validate_cpf(value):
    cpf = re.sub(r'\D', '', value)

    if len(cpf) != 11:
        raise ValidationError('CPF deve conter 11 dígitos')

    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')

    # Valida primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        raise ValidationError('CPF inválido')

    # Valida segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        raise ValidationError('CPF inválido')


def validate_phone(value):
    phone = re.sub(r'\D', '', value)
    if len(phone) not in (10, 11):
        raise ValidationError('Telefone deve conter 10 ou 11 dígitos')


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients_profile')
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_cpf])
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return f'{self.user.name} ({self.cpf})'
