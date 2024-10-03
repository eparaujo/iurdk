from rest_framework import serializers
from classes.models import Aula


class AulaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aula
        fields = '__all__'