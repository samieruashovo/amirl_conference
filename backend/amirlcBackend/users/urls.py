from django.urls import path
from .views import UserDetailView
from .models import User

urlpatterns = [
    path('user/<username>/', UserDetailView.as_view()),
]
