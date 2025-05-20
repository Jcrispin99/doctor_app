from .serializers import *
from .models import Doctor, Departament, DoctorAvailability, MedicalNote, MedicalNote

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView 

class ListDoctorsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DoctorDetailView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class ListDepartamentsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()

class DepartamentDetailView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()

class ListDoctorAvailabilitiesView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class DoctorAvailabilityDetailView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class ListMedicalNotesView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class MedicalNoteDetailView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()