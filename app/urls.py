from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('api/v1/', include('karatecas.urls')),
    path('api/v1/', include('dojos.urls')),
    path('api/v1/', include('karatestyles.urls')),
    path('api/v1/', include('katas.urls')),
    path('api/v1/', include('postures.urls')),
    path('api/v1/', include('senseis.urls')),
    path('api/v1/', include('workouts.urls')),
    path('api/v1/', include('times.urls')),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('reviewsdojos.urls')),
]