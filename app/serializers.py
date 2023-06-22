from rest_framework import serializers
from .models import Company, Device, Employee, DeviceAllocation
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type':'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password':{'write_only':True}
        }

    def validate(self, attrs): 
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
    



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email')



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
