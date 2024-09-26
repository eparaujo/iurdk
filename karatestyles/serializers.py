from rest_framework import serializers
from karatestyles.models import KarateStyle


class KarateStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = KarateStyle
        fields = '__all__'