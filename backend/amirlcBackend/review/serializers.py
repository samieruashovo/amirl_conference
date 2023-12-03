from rest_framework import serializers
from .models import Review
from rest_framework.response import Response


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['__all__']
        extra_kwargs = {'comment': {'required': False}}

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.reviewer = validated_data.get('reviewer', instance.reviewer)
        instance.paper = validated_data.get('paper', instance.paper)
        instance.score = validated_data.get('score', instance.score)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance
