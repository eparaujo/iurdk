from django.urls import path
from . import views

urlpatterns = [
    path('postures/', views.PostureCreateListAPIView.as_view(), name='posture=create-list'),
    path('postures/<int:pk>/', views.PostureRetrieveUpdateDestroyAPIView.as_view(), name='posture-detail-view'),    
]