from rest_framework import serializers
from .models import DoctorAvailability


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorAvailability
        fields = ['id', 'doctor', 'weekday', 'start_time', 'end_time', 'slot_duration', 'is_active']
