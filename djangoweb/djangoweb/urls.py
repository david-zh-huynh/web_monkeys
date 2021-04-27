from . import views, settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
