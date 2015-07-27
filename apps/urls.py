from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers, serializers, viewsets

admin.autodiscover()

from main.views import *


urlpatterns = [
    url(r'^', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('main.urls')),
    url(r'^rest-api/docs/', include('rest_framework_docs.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)