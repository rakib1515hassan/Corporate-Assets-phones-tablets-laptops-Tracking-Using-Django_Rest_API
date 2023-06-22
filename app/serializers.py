from rest_framework import serializers
from .models import Company, Device, Employee, DeviceAllocation
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    CONDITION_CHOICES = [
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Normal', 'Normal'),
    ]
    condition = serializers.ChoiceField(choices=CONDITION_CHOICES, default='Good')
    class Meta:
        model = Device
        fields = ('id', 'name', 'serial_number', 'condition', 'checked_out', 'company')



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DeviceAllocationSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = DeviceAllocation
        fields = '__all__'
