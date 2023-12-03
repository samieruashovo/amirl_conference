from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Paper
from .serializers import PaperSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, exceptions
from rest_framework import viewsets, exceptions

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


# Create your views here.


class PaperListView(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create_paper(self, request):
        if request.method == 'POST':
            serializer = PaperSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            raise exceptions.MethodNotAllowed(request.method)

    @classmethod
    def get_extra_actions(cls):
        return []
