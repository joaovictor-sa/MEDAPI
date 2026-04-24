from django.db import models
from doctors.models import Doctor


class DoctorAvailability(models.Model):
    WEEKDAYS = [
        (0, 'Segunda-Feira'),
        (1, 'Terça-Feira'),
        (2, 'Quarta-Feira'),
        (3, 'Quinta-Feira'),
        (4, 'Sexta-Feira'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    weekday = models.IntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    slot_duration = models.PositiveIntegerField(help_text='Slot duration in minutes')
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('doctor', 'weekday', 'start_time')
