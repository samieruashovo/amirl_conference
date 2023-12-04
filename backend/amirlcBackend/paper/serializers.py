from rest_framework import serializers
from .models import Paper
from users.serializers import UserSerializer


class PaperSerializer(serializers.ModelSerializer):
    authors = UserSerializer(many=True, read_only=True)
    reviewers = UserSerializer(many=True, read_only=True)
    # reviews = serializers.SerializerMethodField()

    class Meta:
        model = Paper
        fields = '__all__'

    # def get_reviews(self, obj):
    #     return obj.reviews.values_list('id', flat=True)

    def get_authors(self, obj):
        return obj.authors.values_list('id', flat=True)

    def get_reviewers(self, obj):
        return obj.reviewers.values_list('id', flat=True)

    def create(self, validated_data):
        paper = Paper.objects.create(**validated_data)
        return paper

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.abstract = validated_data.get('abstract', instance.abstract)
        instance.file = validated_data.get('file', instance.file)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
