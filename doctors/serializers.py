from rest_framework import serializers
from .models import Doctor, Departament, DoctorAvailability, MedicalNote
from datetime import date

class DoctorSerializer(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField()
    class Meta:
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'experience',
            'phone_number',
            'email',
            'address',
            'biography',
            'is_on_vacation',
            'qualification',
            'career_start_date',
        ]
            
    def get_experience(self, obj):
        experience = date.today() - obj.career_start_date
        year =experience.days // 365
        return f"{year} years"

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