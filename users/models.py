from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    expo_push_token = models.CharField(max_length=255, blank=True, null=True)
    
    # Add any additional fields you need
    
    class Meta:
        db_table = 'auth_user' 