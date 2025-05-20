from django.urls import path
from doctors.views import ListDoctorsView,DoctorDetailView, ListDepartamentsView,DepartamentDetailView, ListDoctorAvailabilitiesView, DoctorAvailabilityDetailView, ListMedicalNotesView, MedicalNoteDetailView
urlpatterns = [
    path('doctors', ListDoctorsView.as_view()),
    path('doctors/<int:pk>', DoctorDetailView.as_view()),
    path('departament', ListDepartamentsView.as_view()),
    path('departament/<int:pk>', DepartamentDetailView.as_view()),
    path('doctoravailabilities', ListDoctorAvailabilitiesView.as_view()),
    path('doctoravailabilities/<int:pk>', DoctorAvailabilityDetailView.as_view()),
    path('medicalnotes', ListMedicalNotesView.as_view()),
    path('medicalnotes/<int:pk>', MedicalNoteDetailView.as_view()),
]
