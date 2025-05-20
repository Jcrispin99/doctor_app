from rest_framework import viewsets
from .serializers import DoctorSerializer, DepartamentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Departament, DoctorAvailability, MedicalNote

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DepartamenViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()

class DoctoravailabilitiesViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class MedicalnotesViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()