from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]