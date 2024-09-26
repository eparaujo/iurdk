from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from karatecas.models import Karateca
from karatecas.serializers import KaratecaSerializer


# Create your views here.
class KaratecaCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)    
    queryset = Karateca.objects.all()
    serializer_class = KaratecaSerializer


class KaratecaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)    

    queryset = Karateca.objects.all()
    serializer_class = KaratecaSerializer