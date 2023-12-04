
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/token/',  include('djoser.urls.jwt')),

    path('api/', include('users.urls')),
    path('conference/', include('conference.urls')),
    path('paper/', include('paper.urls')),
    # path('review/', include('review.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
