from rest_framework import serializers
from .models import Company, Device, Employee, DeviceAllocation
from django.contrib.auth import get_user_model
User = get_user_model()

from Account.serializers import UserProfileSerializer



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]
    condition = serializers.ChoiceField(choices=CONDITION_CHOICES, default='New')
    class Meta:
        model = Device
        fields = ('id', 'name', 'serial_number', 'condition', 'company')



class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'



class DeviceAllocationSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer( read_only = True )
    device   = DeviceSerializer( read_only = True )
    class Meta:
        model = DeviceAllocation  
        fields = ( 'id', 'employee', 'device', 'assign_date', 'return_date')
