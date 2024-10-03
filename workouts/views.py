from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission 
from workouts.models import Workout
from workouts.serializers import WorkoutSerializer

# Create your views here.
class WorkoutCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class WorkoutRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer