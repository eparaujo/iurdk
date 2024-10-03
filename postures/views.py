from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from postures.models import Posture
from postures.serializers import PostureSerializer
from app.permissions import GlobalDefaultPermission

# Create your views here.
class PostureCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Posture.objects.all()
    serializer_class = PostureSerializer

class PostureRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Posture.objects.all()
    serializer_class = PostureSerializer