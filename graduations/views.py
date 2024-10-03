from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from graduations.models import Graduation
from graduations.serializers import GraduationSerializer


# Create your views here.
class GraduationCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Graduation.objects.all()
    serializer_class = GraduationSerializer


class GraduationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)    
    queryset = Graduation.objects.all() 
    serializer_class = GraduationSerializer