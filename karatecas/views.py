from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from karatecas.models import Karateca
from karatecas.serializers import karatecaSerializer


# Create your views here.
class KaratecaCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Karateca.objects.all()
    serializer_class = karatecaSerializer


class KaratecaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Karateca.objects.all()
    serializer_class = karatecaSerializer