from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Appointment
from . import serializers
from authentication.permissions import IsAdmin, IsPatient


class AppointmentLisCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.AppointmentSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsPatient()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return Appointment.objects.all()
        if getattr(user, 'role', None) == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        if getattr(user, 'role', None) == 'patient':
            return Appointment.objects.filter(patient__user=user)
        return Appointment.objects.none()


class AppointmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AppointmentSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return Appointment.objects.all()
        if getattr(user, 'role', None) == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        if getattr(user, 'role', None) == 'patient':
            return Appointment.objects.filter(patient__user=user)
        return Appointment.objects.none()

    def perform_update(self, serializer):
        user = self.request.user
        role = getattr(user, 'role', None)
        new_status = serializer.validated_data.get('status')

        if new_status and role == 'patient':
            if new_status != 'canceled':
                raise PermissionDenied('Pacientes só podem cancelar consultas.')

        if new_status and role == 'doctor':
            appointment = self.get_object()
            if appointment.doctor.user != user:
                raise PermissionDenied('Você não pode alterar consultas de outros médicos')
            if new_status != 'completed':
                raise PermissionDenied('Médicos só podem marcar consultas como concluidas')

        serializer.save()
