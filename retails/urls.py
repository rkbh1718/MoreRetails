from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include(more.urls),
    path('admin/', admin.site.urls),
]
