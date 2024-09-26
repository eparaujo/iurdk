from rest_framework import serializers
from postures.models import Posture


class PostureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posture
        fields = '__all__'