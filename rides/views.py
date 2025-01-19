from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from django.utils import timezone
from .models import RideRequest
from .serializers import RideRequestSerializer
from .utils import calculate_distance, send_push_notification

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creators of a ride request to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator of the ride request
        return obj.creator == request.user

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Create the ride request
        self.perform_create(serializer)

        # Find nearby ride requests
        nearby_requests = self.find_nearby_requests(
            start_lat=serializer.validated_data['start_latitude'],
            start_lon=serializer.validated_data['start_longitude'],
            dest_lat=serializer.validated_data['destination_latitude'],
            dest_lon=serializer.validated_data['destination_longitude']
        )

        print(nearby_requests, "nearby_requests")
        # push notification to the user
        
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def find_nearby_requests(self, start_lat, start_lon, dest_lat, dest_lon):
        """Find ride requests with similar start and end points."""
        MAX_DISTANCE = 2.5  # miles
        nearby_requests = []
        
        potential_matches = RideRequest.objects.exclude(
            creator=self.request.user
        ).filter(
            status='new',
            end_time__gt=timezone.now()
        ).select_related('creator')  # Add this to optimize queries
        
        for request in potential_matches:
            start_distance = calculate_distance(
                start_lat, start_lon,
                request.start_latitude, request.start_longitude
            )
            dest_distance = calculate_distance(
                dest_lat, dest_lon,
                request.destination_latitude, request.destination_longitude
            )
            
            if start_distance <= MAX_DISTANCE and dest_distance <= MAX_DISTANCE:
                request_data = self.get_serializer(request).data
                nearby_requests.append(request_data)
                
                # Send push notification to the creator of the matching request
                if request.creator.expo_push_token:
                    creator_type = self.request.data.get('creator_type', 'User')
                    send_push_notification(
                        request.creator.expo_push_token,
                        'New Nearby Ride Request!',
                        f'A {creator_type} is traveling a similar route.',
                        data={
                            'type': 'nearby_ride',
                            'ride_request_id': request_data['request_id'],
                            'start_distance': round(start_distance, 2),
                            'destination_distance': round(dest_distance, 2)
                        }
                    )
        
        # Also notify the current user about matches
        if nearby_requests and self.request.user.expo_push_token:
            send_push_notification(
                self.request.user.expo_push_token,
                'Matching Rides Found!',
                f'Found {len(nearby_requests)} similar ride requests.',
                data={
                    'type': 'matching_rides',
                    'count': len(nearby_requests)
                }
            )
        
        return nearby_requests

    def perform_create(self, serializer):
        # Automatically set the creator when creating a new ride request
        serializer.save(creator=self.request.user)