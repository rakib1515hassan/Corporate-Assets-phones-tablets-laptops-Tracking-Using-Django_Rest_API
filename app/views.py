from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Company, Employee, Device, DeviceAllocation
from app.serializers import CompanySerializer, DeviceSerializer, EmployeeSerializer, DeviceAllocationSerializer



from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


## Create your views here.
class CompanyCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


class CompanyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]