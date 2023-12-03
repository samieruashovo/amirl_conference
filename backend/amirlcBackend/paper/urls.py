from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaperListView

router = DefaultRouter()

router.register(r'', PaperListView, basename='paper')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'paper/', PaperListView.as_view({'get': 'retrieve'}), name='create_paper'),
]
