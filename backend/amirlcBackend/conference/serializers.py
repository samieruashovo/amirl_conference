from rest_framework import serializers
from .models import Conference
from rest_framework.response import Response


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ['__all__']
        extra_kwargs = {'thumbnail': {'required': False}}

    def create(self, validated_data):
        return Conference.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.thumbnail = validated_data.get(
            'thumbnail', instance.thumbnail)
        instance.submission_satrt = validated_data.get(
            'submission_satrt', instance.submission_satrt)
        instance.submission_deadline = validated_data.get(
            'submission_deadline', instance.submission_deadline)
        instance.conference_date = validated_data.get(
            'conference_date', instance.conference_date)
        instance.place = validated_data.get('place', instance.place)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance


class ConferenceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ['name', 'acronym', 'description', 'thumbnail', 'submission_satrt',
                  'submission_deadline', 'conference_date', 'created_at', 'place', 'website']
        extra_kwargs = {'thumbnail': {'required': False}}
