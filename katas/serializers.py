from rest_framework import serializers
from katas.models import Kata


class KataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kata
        fields = '__all__'

class KataStatsSerializer(serializers.Serializer):
    total_katas   = serializers.IntegerField()
    katas_by_styles  = serializers.ListField()
    total_review  = serializers.IntegerField()
    average_stars = serializers.FloatField()
