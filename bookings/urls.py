from django.urls import path
from .views import (
    ListAppointmentsView, AppointmentDetailView,ListMedicalNotesView,MedicalNoteDetailView
)

urlpatterns = [
    path('appointments', ListAppointmentsView.as_view()),
    path('appointments/<int:pk>', AppointmentDetailView.as_view()),
    path('medical_notes', ListMedicalNotesView.as_view()),
    path('medical_notes/<int:pk>', MedicalNoteDetailView.as_view()),
]
