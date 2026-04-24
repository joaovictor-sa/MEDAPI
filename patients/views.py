from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from . import serializers
from authentication.permissions import IsAdmin


class PatientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.PatientSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return Patient.objects.all()
        if getattr(user, 'role', None) == 'patient':
            return Patient.objects.filter(user=user)
        return Patient.objects.none()


class PatientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PatientSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return Patient.objects.all()
        if getattr(user, 'role', None) == 'patient':
            return Patient.objects.filter(user=user)
        return Patient.objects.none()
