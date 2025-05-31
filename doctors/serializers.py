from rest_framework import serializers
from .models import Doctor, Departament, DoctorAvailability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_email(self, value):
        if "example.com" in value:
            return value
        raise serializers.ValidationError("Invalid email domain")

    def validate(self, attrs):
        if len(attrs['phone_number']) != 9 and attrs['is_on_vacation'] == True:
            raise serializers.ValidationError(
                "Por Favor, verificar su numero de telefono"
            )
        return super().validate(attrs)


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'