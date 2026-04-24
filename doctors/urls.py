from django.urls import path
from . import views


urlpatterns = [
    path('doctors/', views.DoctorListCreateAPIView.as_view(), name='doctor-create-list'),
    path('doctors/<int:pk>/', views.DoctorRetrieveUpdateDestroyAPIView.as_view(), name='doctor-detail-view'),

]
