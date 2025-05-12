from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('tailwind/', include('soup.urls')),
    path('bootstrap/', include('program.urls')),
    path('/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
