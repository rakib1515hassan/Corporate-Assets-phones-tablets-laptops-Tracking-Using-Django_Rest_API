from rest_framework import serializers
from .models import Company, Device, Employee, DeviceAllocation


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


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
