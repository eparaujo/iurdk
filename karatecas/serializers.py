from rest_framework import serializers
from karatecas.models import Karateca


class KaratecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Karateca
        fields = '__all__' 