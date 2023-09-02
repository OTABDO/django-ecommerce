from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Urls
    path('admin/', admin.site.urls),
    # Store App
    path('', include('store.urls')),
    # Cart App
    path('cart/', include('cart.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
