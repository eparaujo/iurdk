from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from senseis.models import Sensei
from senseis.serializers import SenseiSerializer


# Create your views here.
class SenseiCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Sensei.objects.all()
    serializer_class = SenseiSerializer


class SenseiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)     

    queryset = Sensei.objects.all()
    serializer_class = SenseiSerializer