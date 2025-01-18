from django.db import models
from django.conf import settings

class RideRequest(models.Model):
    CREATOR_TYPES = [
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('complete', 'Complete'),
    ]
    
    request_id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ride_requests'
    )
    creator_type = models.CharField(max_length=10, choices=CREATOR_TYPES)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES,
        default='new'
    )
    note = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride Request {self.request_id} - {self.creator_type}" 