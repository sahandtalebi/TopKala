from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from TopKala import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TopKala_home.urls')),
    path('', include('TopKala_account.urls')),

]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
