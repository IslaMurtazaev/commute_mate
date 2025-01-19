from django.urls import path
from .views import RegisterView, CustomAuthToken, UserDetailView, update_push_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('update-push-token/', update_push_token, name='update-push-token'),
]