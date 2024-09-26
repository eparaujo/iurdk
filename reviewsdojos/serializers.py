from rest_framework import serializers
from reviewsdojos.models import ReviewDojo


class ReviewDojoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewDojo
        fields = '__all__'