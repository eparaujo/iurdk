from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission 
from weekdays.models import WeekDay
from weekdays.serializers import WeekDaySerializer


# Create your views here.
class WeekDayCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = WeekDay.objects.all()
    serializer_class = WeekDaySerializer


class WeekDayRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = WeekDay.objects.all()
    serializer_class = WeekDaySerializer