from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patient


@receiver(post_save, sender=Patient)
def set_patient_role(sender, instance, created, **kwargs):
    if created:
        instance.user.role = 'patient'
        instance.user.save()
