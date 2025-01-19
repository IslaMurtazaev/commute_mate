from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers
from rides.views import RideRequestViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', include('users.urls')),
    path('rides/', include('rides.urls')),
]
