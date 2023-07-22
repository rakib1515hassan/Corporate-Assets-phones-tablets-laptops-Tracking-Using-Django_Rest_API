from django.urls import path, include
from Assets import views


urlpatterns = [

    ## Company URLs
    path('company/', views.CompanyListCreateView.as_view()),
    path('company/<int:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view()),


    ## Device URLs
    path('devices/', views.DeviceListCreateView.as_view()),
    path('devices/<int:pk>/', views.DeviceRetrieveUpdateDestroyView.as_view()),
    

    ## Employee URLs
    path('employees/', views.EmployeeListCreateView.as_view()),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroyView.as_view()),


    ## Employee Device Allocation
    path('devices-allocation/', views.DeviceAllocationView.as_view()),
    path('devices-allocation/<int:pk>/', views.DeviceAllocationModifyView.as_view()),


    ## Employee Retrieve Hi's Device
    path('employees-allocated-device/<int:pk>/', views.EmployeeAllocationListView.as_view()),


]

