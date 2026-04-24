from django.urls import path
from . import views


urlpatterns = [
    path('specialties/', views.SpecialtyListCreateAPIView.as_view(), name='specialty-create-list'),
    path('specialties/<int:pk>/', views.SpecialtyRetrieveUpdateDestroyApiView.as_view(), name='specialty-detail-view'),

]
