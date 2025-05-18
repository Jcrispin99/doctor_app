from django.urls import path
from patients.views import ListPatientsView, PatientDetailView

urlpatterns = [
    path('patients', ListPatientsView.as_view()),
    path('patients/<int:pk>', PatientDetailView.as_view()),
]
