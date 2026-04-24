from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views


urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', views.RegisterCreateAPIView.as_view(), name='register'),
]
