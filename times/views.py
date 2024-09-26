from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from times.models import Time
from times.serializers import TimeSerializer


class TimeCreateListAPIView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class TimeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
