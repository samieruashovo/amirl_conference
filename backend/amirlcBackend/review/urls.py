from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()

router.register(r'', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'review/', ReviewViewSet.as_view({'get': 'retrieve'}), name='create_review'),
]
