from django.urls import path
from . import views


urlpatterns = [
    path('appointments/', views.AppointmentLisCreateAPIView.as_view(), name='appointments-create-list'),
    path('appointments/<int:pk>/', views.AppointmentRetrieveUpdateDestroyAPIView.as_view(), name='appointments-detail-view'),
]
