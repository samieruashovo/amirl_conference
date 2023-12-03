from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewListView

router = DefaultRouter()

router.register(r'', ReviewListView, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'review/', ReviewListView.as_view({'get': 'retrieve'}), name='create_review'),
]
