from datetime import datetime, timedelta
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import DoctorAvailability
from . import serializers
from authentication.permissions import IsAdmin
from appointments.models import Appointment


class AvailabilityListCreateApiView(generics.ListCreateAPIView):
    serializer_class = serializers.AvailabilitySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return DoctorAvailability.objects.all()
        if getattr(user, 'role', None) == 'doctor':
            return DoctorAvailability.objects.filter(doctor__user=user)
        return DoctorAvailability.objects.none()


class AvailabilityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AvailabilitySerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return DoctorAvailability.objects.all()
        if getattr(user, 'role', None) == 'doctor':
            return DoctorAvailability.objects.filter(doctor__user=user)
        return DoctorAvailability.objects.none()


class AvailableSlotsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctor_id = request.query_params.get('doctor')
        date_str = request.query_params.get('date')

        if not doctor_id or not date_str:
            return Response({'error': 'Parâmetros doctor e date são obrigatórios'}, status=400)

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Formato de data inválido. Use YYYY-MM-DD'}, status=400)

        weekday = date.weekday()

        availabilities = DoctorAvailability.objects.filter(
            doctor_id=doctor_id,
            weekday=weekday,
            is_active=True,
        )

        if not availabilities.exists():
            return Response({'slots': []})

        booked = set(
            Appointment.objects.filter(
                doctor_id=doctor_id,
                date=date,
                status='schedule',
            ).values_list('start_time', flat=True)
        )

        slots = []
        for availability in availabilities:
            current = datetime.combine(date, availability.start_time)
            end = datetime.combine(date, availability.end_time)
            delta = timedelta(minutes=availability.slot_duration)

            while current + delta <= end:
                if current.time() not in booked:
                    slots.append(current.strftime('%H:%M'))
                current += delta

        return Response({'slots': slots})
