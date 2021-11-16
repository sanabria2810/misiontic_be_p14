from django.shortcuts import render
from rest_framework import generics
from.models import PQR, Soporte
from serializer import SoporteSerializer, PQRSerializer
# Create your views here.

class SoporteListCreate(generics.ListCreateApiView):
    queryset = Soporte.objects.all()
    serializers_class = SoporteSerializer


class SoporteUpdateDelete(generics.RetrieveDestroyAPIView):
    queryset = Soporte.objects.all()
    serializers_class = SoporteSerializer

class PQRListCreate(generics.ListCreateApiView):
    queryset = PQR.objects.all()
    serializers_class = PQRSerializer    

class PQRUpdateDelete(generics.RetrieveDestroyAPIView):
    queryset = PQR.objects.all()
    serializers_class = PQRSerializer