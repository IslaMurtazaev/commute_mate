from rest_framework import serializers
from .models import RideRequest

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = [
            'request_id', 
            'creator_id', 
            'creator_type',
            'start_location',
            'end_location',
            'start_time',
            'end_time',
            'status',
            'created_at',
            'updated_at'
        ] 