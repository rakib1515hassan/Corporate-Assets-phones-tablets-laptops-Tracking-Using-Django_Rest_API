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
class CompanyListCreateView(generics.ListCreateAPIView):
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



class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]



class DeviceAllocationView(generics.UpdateAPIView):
    queryset = DeviceAllocation.objects.all()
    serializer_class = DeviceAllocationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


#__________________________________________________________________




# Employee Views----------------------------------------------------
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# Only employee see this information not update or delete
class EmployeeAllocationListView(generics.ListAPIView):
    serializer_class = DeviceAllocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return DeviceAllocation.objects.filter(employee=employee_id)

#__________________________________________________________________