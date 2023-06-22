from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Company, Employee, Device, DeviceAllocation
from app.serializers import (
    UserSerializer, CompanySerializer, DeviceSerializer, EmployeeSerializer, DeviceAllocationSerializer
)



from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveAPIView

## Create your views here.

class UserAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    

# Company Views----------------------------------------------------
class CompanyCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]




class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
#__________________________________________________________________


# Device Views----------------------------------------------------
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#__________________________________________________________________