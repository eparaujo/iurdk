from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from reviewsdojos.models import ReviewDojo
from app.permissions import GlobalDefaultPermission
from reviewsdojos.serializers import ReviewDojoSerializer


# Create your views here.
class ReviewDojoListCreateAPIView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset           = ReviewDojo.objects.all()
    serializer_class   = ReviewDojoSerializer

class ReviewDojoRetrieveUpdareDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset           = ReviewDojo.objects.all()
    serializer_class   = ReviewDojoSerializer