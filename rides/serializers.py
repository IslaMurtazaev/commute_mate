from rest_framework import serializers
from .models import RideRequest
from django.contrib.auth import get_user_model

User = get_user_model()

class RideRequestSerializer(serializers.ModelSerializer):
    creator_first_name = serializers.CharField(source='creator.first_name', read_only=True)
    creator_last_name = serializers.CharField(source='creator.last_name', read_only=True)
    
    class Meta:
        model = RideRequest
        fields = [
            'request_id',
            'creator_first_name',
            'creator_last_name',
            'creator_type',
            'start_location',
            'start_latitude',
            'start_longitude',
            'destination_location',
            'destination_latitude',
            'destination_longitude',
            'start_time',
            'end_time',
            'status',
            'note',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['request_id', 'creator_first_name', 'creator_last_name', 'created_at', 'updated_at']