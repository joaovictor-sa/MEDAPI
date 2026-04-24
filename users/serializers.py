from rest_framework import serializers
from .models import User
from patients.models import Patient
from patients.models import validate_cpf, validate_phone


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # Campos opcionais do Patient
    cpf = serializers.CharField(write_only=True, required=False, validators=[validate_cpf])
    phone = serializers.CharField(write_only=True, required=False, validators=[validate_phone])
    date_of_birth = serializers.DateField(write_only=True, required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password', 'cpf', 'phone', 'date_of_birth']

    def validate(self, data):
        if data.get('role') == 'patient':
            for field in ['cpf', 'phone', 'date_of_birth', 'email']:
                if not data.get(field):
                    raise serializers.ValidationError(
                        {field: 'Este campo é obrigatório para pacientes.'}
                    )
        return data

    def create(self, validated_data):
        patient_fields = {
            'cpf': validated_data.pop('cpf', None),
            'phone': validated_data.pop('phone', None),
            'date_of_birth': validated_data.pop('date_of_birth', None),
        }

        user = User.objects.create_user(**validated_data)

        if user.role == 'patient':
            Patient.objects.create(
                user=user,
                email=user.email,
                **patient_fields
            )

        return user
