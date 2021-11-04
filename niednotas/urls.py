from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('notas.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]
