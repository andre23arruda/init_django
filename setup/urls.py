from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # media

from .api import api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_example/', include('app_example.urls')),
    path('stock/', include('stock_prices.urls')),
]
urlpatterns += api_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media
