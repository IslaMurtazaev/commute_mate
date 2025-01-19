from rest_framework import serializers
from .models import RideRequest
from django.contrib.auth import get_user_model
from decimal import Decimal, ROUND_DOWN

User = get_user_model()

class CoordinateField(serializers.DecimalField):
    def __init__(self, **kwargs):
        super().__init__(max_digits=9, decimal_places=6, **kwargs)

    def to_internal_value(self, data):
        """Convert the input value to a Decimal with 6 decimal places"""
        try:
            return Decimal(str(data)).quantize(Decimal('.000001'), rounding=ROUND_DOWN)
        except (TypeError, ValueError):
            self.fail('invalid')

class RideRequestSerializer(serializers.ModelSerializer):
    creator_first_name = serializers.CharField(source='creator.first_name', read_only=True)
    creator_last_name = serializers.CharField(source='creator.last_name', read_only=True)
    start_latitude = CoordinateField()
    start_longitude = CoordinateField()
    destination_latitude = CoordinateField()
    destination_longitude = CoordinateField()
    
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
