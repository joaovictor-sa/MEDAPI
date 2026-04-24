from django.urls import path
from . import views


urlpatterns = [
    path('availability/', views.AvailabilityListCreateApiView.as_view(), name='availability-create-list'),
    path('availability/<int:pk>/', views.AvailabilityRetrieveUpdateDestroyAPIView.as_view(), name='availability-detail-view'),

]
