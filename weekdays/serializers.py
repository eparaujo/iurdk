from rest_framework import serializers
from weekdays.models import WeekDay


class WeekDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeekDay
        fields = '__all__' 