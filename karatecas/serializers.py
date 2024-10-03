from rest_framework import serializers
from karatecas.models import Karateca


class karatecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Karateca
        fields = '__all__'