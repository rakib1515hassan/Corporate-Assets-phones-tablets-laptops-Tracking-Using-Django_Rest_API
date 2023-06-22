from django.contrib import admin
from app.models import Company, Device, Employee, DeviceAllocation

# Register your models here.



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'address', 'phone_number' )




@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'company', 'serial_number', 'condition', 'checked_out')




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ( 'id' ,'get_username', 'get_email', 'company', 'get_devices', 'get_devices_serial' )

    def get_username(self, obj):
        return obj.user.username
    
    def get_email(self, obj):
        return obj.user.email
    
    get_username.short_description = 'Username'
    get_email.short_description = 'Email'




@admin.register(DeviceAllocation)
class DeviceAssignmentAdmin(admin.ModelAdmin):
    list_display = ( 'id' ,'device', 'employee', 'given_date', 'updated_at', 'return_date' )
