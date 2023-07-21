from django.contrib import admin
from Assets.models import Company, Device, Employee, DeviceAllocation

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'address')




@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'company', 'serial_number', 'condition')




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ( 'id' ,'get_username', 'get_email', 'company')

    def get_username(self, obj):
        return obj.user.username
    
    def get_email(self, obj):
        return obj.user.email
    
    get_username.short_description = 'Username'
    get_email.short_description = 'Email'




@admin.register(DeviceAllocation)
class DeviceAssignmentAdmin(admin.ModelAdmin):
    list_display = ( 'id' ,'device', 'employee', 'assign_date', 'return_date' )

