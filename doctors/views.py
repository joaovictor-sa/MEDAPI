from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from . import serializers
from authentication.permissions import IsAdmin


class DoctorListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DoctorSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return Doctor.objects.all()
        if getattr(user, 'role', None) == 'doctor':
            return Doctor.objects.filter(user=user)
        return Doctor.objects.none()


class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DoctorSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return Doctor.objects.all()
        if getattr(user, 'role', None) == 'doctor':
            return Doctor.objects.filter(user=user)
        return Doctor.objects.none()
