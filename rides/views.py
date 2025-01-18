from rest_framework import viewsets, permissions
from .models import RideRequest
from .serializers import RideRequestSerializer

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

    def perform_create(self, serializer):
        # Automatically set the creator when creating a new ride request
        serializer.save(creator=self.request.user) 