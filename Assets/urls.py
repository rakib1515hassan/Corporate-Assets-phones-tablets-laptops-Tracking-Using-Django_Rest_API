from django.urls import path, include
from Assets import views


urlpatterns = [

    ## Company URLs
    path('company/', views.CompanyListCreateView.as_view()),
    path('company/<int:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view()),

    # # Device URLs
    # path('devices-create/', DeviceListCreateView.as_view(), name='device-list-create'),
    # path('devices-update/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
    # path('devices-allocation-update/<int:pk>/', DeviceAllocationView.as_view(), name='device-allocation'),


    # # Employee URLs
    # path('employees-create/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    # path('employees-update/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    # path('employees-device-allocation/<int:pk>/', EmployeeAllocationListView.as_view(), name='employee-allocation'),





    # # for api authentications
    # path('api-auth/', include('rest_framework.urls')),
]

