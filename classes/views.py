from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from classes.models import Aula
from classes.serializers import AulaSerializer


# Create your views here.
class AulaCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer


class AulaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer