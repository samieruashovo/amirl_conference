from django.shortcuts import render, redirect

from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ConferenceSerializer, ConferenceViewSerializer
from .models import Conference
from users.models import User
from .permissions import ConferencePermissions

# Create your views here.


class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceViewSerializer
    # permission_classes = [ConferencePermissions]

    def get_queryset(self):
        queryset = Conference.objects.all()
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def create_conference(self, request):
        if request.method == 'POST':
            serializer = ConferenceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            raise exceptions.MethodNotAllowed(request.method)
