from rest_framework import serializers
from graduations.models import Graduation


class GraduationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Graduation
        fields = '__all__' 