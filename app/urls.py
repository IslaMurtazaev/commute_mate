from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from rides.views import RideRequestViewSet

router = routers.DefaultRouter()
router.register(r'ride-requests', RideRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', include('users.urls')),
]
