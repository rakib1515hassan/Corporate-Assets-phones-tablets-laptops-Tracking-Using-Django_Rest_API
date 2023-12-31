from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class User_OTP(models.Model):
    user       = models.OneToOneField( User, on_delete=models.CASCADE )
    otp        = models.IntegerField()
    created_at = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return self.user.username
    