from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from postures.models import Posture
from postures.serializers import PostureSerializer

# Create your views here.
class PostureCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Posture.objects.all()
    serializer_class = PostureSerializer

class PostureRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Posture.objects.all()
    serializer_class = PostureSerializer