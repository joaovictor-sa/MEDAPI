from rest_framework import serializers
from .models import Patient, validate_cpf
from users.serializers import UserSerializer
from users.models import User


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    cpf = serializers.CharField(validators=[validate_cpf])

    class Meta:
        model = Patient
        fields = ['id', 'user', 'user_id', 'cpf', 'phone', 'date_of_birth', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
