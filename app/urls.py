from django.urls import path, include
from rest_framework_simplejwt.views import (
            TokenObtainPairView,
            TokenRefreshView,
        )
from rest_framework_simplejwt.views import TokenVerifyView
from app.views import *



urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # For TokenVerifyView
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('user/', UserAPIView.as_view(), name='user'),

    # Company URLs
    path('company-create/', CompanyListCreateView.as_view(), name='company-create-view'),
    path('company_update/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company_update-view'),

    # Device URLs
    path('devices-create/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices-update/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
    path('devices-allocation-update/<int:pk>/', DeviceAllocationView.as_view(), name='device-allocation'),


    # Employee URLs
    path('employees-create/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees-update/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('employees-device-allocation/<int:pk>/', EmployeeAllocationListView.as_view(), name='employee-allocation'),





    # for api authentications
    path('api-auth/', include('rest_framework.urls')),
]

