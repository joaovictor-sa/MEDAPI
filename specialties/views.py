from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import SpecialtySerializer
from .models import Specialty
from authentication.permissions import IsAdmin


class SpecialtyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]


class SpecialtyRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecialtySerializer
    queryset = Specialty.objects.all()

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATH', 'DELETE']:
            return [IsAdmin()]
        return [IsAuthenticated()]
