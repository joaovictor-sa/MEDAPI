from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from . import serializers
from authentication.permissions import IsAdmin


User = get_user_model()


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return User.objects.all()
        return User.objects.filter(id=user.id)


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'role', None) == 'admin':
            return User.objects.all()
        return User.objects.filter(id=user.id)
