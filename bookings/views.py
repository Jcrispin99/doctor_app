from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Appointment, MedicalNote
from.serializers import AppointmentSerializer, MedicalNoteSerializer

class ListAppointmentsView(ListAPIView, CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ListMedicalNotesView(ListAPIView, CreateAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer

class MedicalNoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer    
    