from rest_framework import serializers
from dojos.models import Dojo


class DojoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dojo
        fields = '__all__'