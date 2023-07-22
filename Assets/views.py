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
## URL = ( http://127.0.0.1:8000/assets/devices/ )
class DeviceListCreateView(generics.ListCreateAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


## URL = ( http://127.0.0.1:8000/assets/devices/<int:pk>/)
class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

# #__________________________________________________________________




# # Employee Views----------------------------------------------------
## URL = ( http://127.0.0.1:8000/assets/employees/)
class EmployeeListCreateView(generics.ListCreateAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()



## URL = ( http://127.0.0.1:8000/assets/employees/<int:pk>/)
class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()




## URL = ( http://127.0.0.1:8000/assets/devices-allocation/)
class DeviceAllocationView(generics.ListCreateAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = DeviceAllocationSerializer
    queryset = DeviceAllocation.objects.all()




## URL = ( http://127.0.0.1:8000/assets/devices-allocation/<int:pk>/)
class DeviceAllocationModifyView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = DeviceAllocationSerializer
    queryset = DeviceAllocation.objects.all()


#__________________________________________________________________



## Only employee see this information not update or delete-----------------

## URL = ( http://127.0.0.1:8000/assets/employees-allocated-device/<int:pk>/)
class EmployeeAllocationListView(generics.RetrieveAPIView):
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DeviceAllocationSerializer

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        emp_obj = Employee.objects.filter(id = employee_id).first()
        if self.request.user == emp_obj.user:
            return DeviceAllocation.objects.filter(employee=employee_id)

    