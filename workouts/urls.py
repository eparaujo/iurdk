from django.urls import path
from . import views

urlpatterns = [
    path('workouts/', views.WorkoutCreateListAPIView.as_view(), name='workout-create-list'),
    path('workouts/<int:pk>/', views.WorkoutRetrieveUpdateDestroyAPIView.as_view(), name='workout-detail-view'),    
]