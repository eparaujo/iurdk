from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from karatestyles.serializers import KarateStyleSerializer
from karatestyles.models import KarateStyle
from app.permissions import GlobalDefaultPermission


class KarateStyleCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = KarateStyle.objects.all()
    serializer_class = KarateStyleSerializer

class KarateStyleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)        
    queryset = KarateStyle.objects.all()
    serializer_class = KarateStyleSerializer
