from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from dojos.models import Dojo
from dojos.serializers import DojoSerializer


# Create your views here.
class DojoCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Dojo.objects.all()
    serializer_class = DojoSerializer


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Dojo.objects.all()
    serializer_class = DojoSerializer