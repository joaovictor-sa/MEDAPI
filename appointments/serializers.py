from datetime import datetime, timedelta
from rest_framework import serializers
from .models import Appointment
from availability.models import DoctorAvailability


VALID_TRANSITIONS = {
    'scheduled': ['completed', 'canceled'],
    'completed': [],
    'canceled': [],
}


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'start_time', 'end_time', 'status', 'created_at']
        read_only_fields = ['end_time', 'created_at']

    def validate_status(self, value):
        if self.instance:
            current_status = self.instance.status
            allowed = VALID_TRANSITIONS.get(current_status, [])
            if value not in allowed:
                raise serializers.ValidationError(
                    f"Transição inválida: '{current_status}' → '{value}'."
                )

            if value == 'canceled':
                appointment_dt = datetime.combine(self.instance.date, self.instance.start_time)
                if appointment_dt - datetime.now() < timedelta(hours=24):
                    raise serializers.ValidationError('A consulta só pode ser cancelada com no mínimo 24H de antecedência.')

        return value

    def validate(self, data):
        if self.instance:
            return data

        doctor = data['doctor']
        date = data['date']
        start_time = data['start_time']
        weekday = date.weekday()

        availability = DoctorAvailability.objects.filter(
            doctor=doctor,
            weekday=weekday,
            start_time__lte=start_time,
            end_time__gte=start_time,
        ).first()

        if not availability:
            raise serializers.ValidationError('O médico não tem disponibilidade nesse horário.')

        duration = timedelta(minutes=availability.slot_duration)
        start_dt = datetime.combine(date, start_time)
        end_time = (start_dt + duration).time()

        conflict = Appointment.objects.filter(
            doctor=doctor,
            date=date,
            status='scheduled',
            start_time__lt=end_time,
            end_time__gt=start_time,
        ).exists()

        if conflict:
            raise serializers.ValidationError('Já existe uma consulta agendada nesse horário.')

        data['end_time'] = end_time
        return data
