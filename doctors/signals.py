from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Doctor


@receiver(post_save, sender=Doctor)
def set_doctor_role(sender, instance, created, **kwargs):
    if created:
        instance.user.role = 'doctor'
        instance.user.save()
