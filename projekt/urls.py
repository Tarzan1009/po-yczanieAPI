
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include('APIlend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
