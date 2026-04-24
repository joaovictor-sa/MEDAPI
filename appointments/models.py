from django.db import models
from doctors.models import Doctor
from patients.models import Patient


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Agendada'),
        ('canceled', 'Cancelada'),
        ('completed', 'Concluída'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'date', 'start_time')
