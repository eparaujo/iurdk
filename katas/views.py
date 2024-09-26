from katas.serializers import KataSerializer, KataStatsSerializer
from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from katas.models import Kata
from reviews.models import Review

# Create your views here.
class KataCreateListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)    
    queryset = Kata.objects.all()
    serializer_class = KataSerializer

class KataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)    
    queryset = Kata.objects.all()
    serializer_class = KataSerializer

class KataStatsView(views.APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Kata.objects.all()

    def get(self, request):
        total_katas = self.queryset.count()
        #katas_styles = self.queryset.values('karatestyles__style').annotate(count=Count('id'))
        total_review = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data={
            'total_katas': total_katas,
            #'katas_styles': katas_styles,
            'total_review': total_review,
            'average_stars': round(average_stars, 2) if average_stars else 0,
        }

        serializer = KataStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        return response.Response(data=serializer.validated_data, status=status.HTTP_200_OK)