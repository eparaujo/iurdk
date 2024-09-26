from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from senseis.models import Sensei
from senseis.serializers import SenseiSerializer

# Create your views here.
class SenseiListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sensei.objects.all()
    serializer_class = SenseiSerializer

class SenseiRetrireveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sensei.objects.all()
    serializer_class = SenseiSerializer