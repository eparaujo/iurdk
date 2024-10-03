from rest_framework import serializers
from senseis.models import Sensei


class SenseiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensei
        fields = '__all__' 