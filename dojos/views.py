from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from dojos.models import Dojo
from dojos.serializers import DojoSerializer, DojoListDetailSerializer
from app.permissions import GlobalDefaultPermission
from senseis.models import Sensei


class DojoCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)    
    queryset = Dojo.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DojoListDetailSerializer
        return DojoSerializer

class DojoRetrieveUpdateDesctroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)    
    queryset = Dojo.objects.all()
    serializer_class = DojoSerializer

class DojoStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Dojo.objects.all()

    def get(self, request):
        return response.Response(
            data={'message': 'Consulta de estatística de Dojo'},
            status=status.HTTP_200_OK,
        )