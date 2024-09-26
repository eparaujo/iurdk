from rest_framework import serializers
from dojos.models import Dojo
from senseis.serializers import SenseiSerializer
from times.serializers import TimeSerializer

class DojoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dojo
        fields = '__all__'

class DojoListDetailSerializer(serializers.ModelSerializer):
    sensei = SenseiSerializer()
    #times   = TimeSerializer(many=True)

    class Meta:
        model = Dojo
        fields = [
            'id', 'name', 'site', 'phone', 'email', 'street', 'number', 'zipcode', 'district', 'city', 'state', 'sensei'
        ]