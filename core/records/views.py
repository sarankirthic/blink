from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Department
from .serializers import PatientSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
