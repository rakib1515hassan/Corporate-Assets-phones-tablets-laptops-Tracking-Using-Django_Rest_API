from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()

from Assets.models import Company, Employee, Device, DeviceAllocation
from Assets.serializers import (
    CompanySerializer,
    DeviceSerializer,
    EmployeeSerializer,
    DeviceAllocationSerializer, 
)


from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser
)
from rest_framework.views import APIView

from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

## Create your views here.
# Company Views----------------------------------------------------
## URL = ( http://127.0.0.1:8000/assets/company/ )
class CompanyListCreateView(generics.ListCreateAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()



## URL = ( http://127.0.0.1:8000/assets/company/<int:pk>/ )
class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
# #__________________________________________________________________





# # Device Views----------------------------------------------------
# class DeviceListCreateView(generics.ListCreateAPIView):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]



# class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]



# class DeviceAllocationView(generics.UpdateAPIView):
#     queryset = DeviceAllocation.objects.all()
#     serializer_class = DeviceAllocationSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]


# #__________________________________________________________________




# # Employee Views----------------------------------------------------
# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]


# class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]


# # Only employee see this information not update or delete
# class EmployeeAllocationListView(generics.ListAPIView):
#     serializer_class = DeviceAllocationSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         employee_id = self.kwargs['pk']
#         return DeviceAllocation.objects.filter(employee=employee_id)

#__________________________________________________________________