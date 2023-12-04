from rest_framework import serializers
from .models import Review
from rest_framework.response import Response


from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {'comment': {'required': False}}
