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



    # Company URLs
    path('company-create/', CompanyCreateView.as_view(), name='company-create-view'),
    path('company_update/<int:pk>/', CompanyUpdateView.as_view(), name='company_update-view'),
]
