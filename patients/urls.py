from django.urls import path
from . import views


urlpatterns = [
    path('patients/', views.PatientListCreateAPIView.as_view(), name='patient-create-list'),
    path('patients/<int:pk>/', views.PatientRetrieveUpdateDestroyAPIView.as_view(), name='patient-detail-view'),

]
