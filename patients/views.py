import stat
from .serializers import PatientSerializer
from .models import Patient

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView 

class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class PatientDetailView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()