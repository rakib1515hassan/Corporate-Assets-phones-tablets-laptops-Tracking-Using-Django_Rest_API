from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Company(models.Model):
    name         = models.CharField( max_length=200 )
    address      = models.CharField( max_length=200 )
    phone_number = models.CharField( max_length=16, unique=True )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    



class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name          = models.CharField( max_length=100 )
    serial_number = models.CharField( max_length=100, unique=True )
    condition     = models.CharField( max_length=50, choices=(
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Normal', 'Normal'),
    ) ,default='Good' )

    checked_out   = models.BooleanField( default=False )
    
    class Meta:
        ordering = ['serial_number']

    def __str__(self):
        return self.name
    






class Employee(models.Model):
    user    = models.OneToOneField( User, on_delete=models.CASCADE )
    company = models.ForeignKey( Company, on_delete=models.CASCADE )

    devices = models.ManyToManyField(Device)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.get_full_name()
    
    def get_devices(self):
        return ", ".join([str(device) for device in self.devices.all()])
    
    def get_devices_serial(self):
        return ", ".join([str(device.serial_number) for device in self.devices.all()])
    
    





class DeviceAllocation(models.Model):
    device      = models.ForeignKey( Device, on_delete=models.CASCADE )
    employee    = models.ForeignKey( Employee, on_delete=models.CASCADE )

    updated_at  = models.DateTimeField( auto_now_add=True )
    given_date  = models.DateTimeField( null=True, blank=True )
    return_date = models.DateTimeField( null=True, blank=True )

    class Meta:
        ordering = ['-updated_at']


    def __str__(self):
        if self.return_date:
            return f"{self.employee.user.get_username()} returned {self.device.name}, at: ({self.return_date.ctime()})"
        
        return f"{self.employee.user.get_username()} got {self.device.name}, at: ({self.given_date.ctime()})"
