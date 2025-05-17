from django.contrib import admin
from django.urls import path
from patients.views import lit_patient, patient_detail

urlpatterns = [
    path('patients', lit_patient),
    path('patients/<int:pk>', patient_detail, name='patient_detail'),
]
