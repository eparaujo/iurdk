from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission 
from turnos.models import Turno
from turnos.serializers import TurnoSerializer


# Create your views here.
class TurnoCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


class TurnoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer