from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


# Create your views here.

class UserDetailView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
