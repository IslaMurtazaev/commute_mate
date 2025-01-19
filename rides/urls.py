from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideRequestViewSet

router = DefaultRouter()
router.register(r'requests', RideRequestViewSet, basename='ride-request')

urlpatterns = [
    path('', include(router.urls)),
] 