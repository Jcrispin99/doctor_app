from django.db import router
from django.urls import path
#from doctors.views import ListDoctorsView,DoctorDetailView, ListDepartamentsView,DepartamentDetailView, ListDoctorAvailabilitiesView, DoctorAvailabilityDetailView, ListMedicalNotesView, MedicalNoteDetailView
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet, DepartamenViewSet, DoctoravailabilitiesViewSet, MedicalnotesViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departaments', DepartamenViewSet)
router.register('doctor-availabilities', DoctoravailabilitiesViewSet)
router.register('medical-notes', MedicalnotesViewSet)
urlpatterns = router.urls

