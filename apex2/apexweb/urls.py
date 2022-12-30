from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('post/<slug:url>', post),
    path('category/<slug:url>', category),
    path('tinymce/', include('tinymce.urls')),
]