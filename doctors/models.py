from django.db import models
from django.conf import settings


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='medico')
    specialty = models.ForeignKey('specialties.Specialty', on_delete=models.PROTECT, related_name='medicos')
    crm = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
