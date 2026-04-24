from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('specialties.urls')),
    path('api/v1/', include('patients.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('doctors.urls')),
    path('api/v1/', include('availability.urls')),
    path('api/v1/', include('appointments.urls')),
    path('api/v1/', include('authentication.urls')),

    # Documentação
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
