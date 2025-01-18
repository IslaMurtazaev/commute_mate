from rest_framework import viewsets
from .models import RideRequest
from .serializers import RideRequestSerializer
from rest_framework.permissions import IsAuthenticated

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [IsAuthenticated] 