from rest_framework import viewsets
from .serializers import DoctorSerializer, DepartamentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Departament, DoctorAvailability, MedicalNote
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsDoctor

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated, IsDoctor]

    @action(detail=True, methods=['POST'])# Definir que metodo se va a utilizar con detaill decimos si va a aser un detalle o una lista, detail tru hace acciones en un solo item 
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status":"Doctor is now on vacation"})

    @action(detail=True, methods=['POST'])
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status":"Doctor is available"})

class DepartamenViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class DoctoravailabilitiesViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class MedicalnotesViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

