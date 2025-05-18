import stat
from .serializers import PatientSerializer
from .models import Patient

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView # depende de lo que requiera en la API

class ListPatientsView(ListAPIView, CreateAPIView):#explicame que pasa de fondo ya que no entiendo
    #al importar ListAPIView y CreateAPIView, se puede usar el metodo get y post cosa que simplifica más el codigo
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


    # def post(self, request):
    #     serializer = PatientSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)

class PatientDetailView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()